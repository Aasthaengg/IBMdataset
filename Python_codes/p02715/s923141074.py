n,k=map(int,input().split())
mod = 1000000007
ko = [0]*100005
ans = 0
for i in range(k,0,-1):
    baisu = k//i
    ko[i] = pow(baisu,n,mod)
    for j in range(2,baisu+1):
        ko[i] -= ko[i*j]
        ko[i] %= mod
    ans += ko[i] * i % mod
    ans %= mod
print(ans)
