n,k = map(int,input().split())
ls = list(map(int,input().split()))
di = [0]*2001
sm = 0
ans = 0
cnt = 0
mod = 10**9+7
f = sorted(list(set(ls)))
for i in f:
    di[i] = sm
    sm += ls.count(i)
for j in range(n):
    for l in range(j+1,n):
        if ls[j] > ls[l]:
            cnt += 1
    ans += (cnt*k+di[ls[j]]*k*(k-1)//2)
    if ans >= 10**9+7:
        ans %= mod
    cnt = 0
print(ans)