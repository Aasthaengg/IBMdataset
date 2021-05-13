import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,x = map(int, input().split())
a = list(map(int, input().split()))
def sub(p,q):
    if p+q<=x:
        ans = (0, (p,q))
    elif (p+q-x)<=q:
        ans = (p+q-x, (p, x-p))
    else:
        ans = (p+q-x, (x, 0))
    return ans
ans = 0
a1,a2 = a[:2]
num, (a1,a2) = sub(a1,a2)
ans += num
for i in range(n-2):
    a1,a2 = a2, a[i+2]
    num, (a1,a2) = sub(a1,a2)
    ans += num
print(ans)