import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


### 木の読み込み tree

n,q = map(int, input().split())
ns = [[] for _ in range(n)]
for _ in range(n-1):
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    ns[u].append(v)
    ns[v].append(u)
vals = [0]*n
for _ in range(q):
    p,x = map(int, input().split())
    vals[p-1] += x
ans = [0]*n
done = [False]*n
s = [(0, vals[0])]
done[0] = True
while s:
    u,val = s.pop()
    ans[u] = val
    for v in ns[u]:
        if done[v]:
            continue
        done[v] = True
        s.append((v, val+vals[v]))
write(" ".join(map(str, ans)))