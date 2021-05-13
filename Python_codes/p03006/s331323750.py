import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
xys = [None]*n
for i in range(n):
    x,y = map(int, input().split())
    xys[i] = (x,y)

def sub(p,q):
    seen = [False]*n
    ans = 0
    for start in range(n):
        if seen[start]:
            continue
        ans += 1
        qq = [start]
        seen[start] = True
        while qq:
            u = qq.pop()
            for i,(x,y) in enumerate(xys):
                if seen[i]:
                    continue
#                 print(xys[u][1], y, p, q)
                if (xys[u][0]-x, xys[u][1]-y) == (p,q) or (xys[u][0]-x, xys[u][1]-y) == (-p,-q):
                    qq.append(i)
                    seen[i] = True
    return ans
ans = 10**10
for i in range(n):
    for j in range(n):
        p = xys[i][0]-xys[j][0]
        q = xys[i][1]-xys[j][1]
        val = sub(p,q)
        ans = min(ans, val)
print(ans)