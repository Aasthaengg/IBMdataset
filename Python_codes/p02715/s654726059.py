n,k = [int(x) for x in input().split()]
li = [0]*(k+1)
mod = 10**9+7

ans = 0
for i in range(1,k+1)[::-1]:
    x = pow(k//i,n,mod)
    for j in range(i*2,k+1,i):
        if j%i==0:
            x -= li[j]
    li[i] = x
    ans = (ans+(x*i)%mod)%mod
print(ans%mod)