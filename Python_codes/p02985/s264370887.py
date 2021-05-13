n,k = map(int,input().split())
mod = 10**9 + 7
path = [set() for _ in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    path[a].add(b)
    path[b].add(a)
fac = [1]*(k+2)
fac_inv = [1]*(k+2)
for i in range(1,k+2):
    fac[i] = fac[i-1] * i %mod
    fac_inv[i] = pow(fac[i],mod-2,mod)

def P(n,k):
    if n-k < 0:
        print(0)
        exit()
    return fac[n] * fac_inv[n-k] %mod

ans = 1
reach = [False] * n
reach[0] = True
que = []
for i in path[0]:
    que.append(i)
ans *= P(k,len(path[0])+1)
while que:
    p = que.pop()
    reach[p] = True
    ans *= P(k-2,len(path[p])-1)
    ans %= mod
    for i in path[p]:
        if not reach[i]:
            que.append(i)
print(ans)
