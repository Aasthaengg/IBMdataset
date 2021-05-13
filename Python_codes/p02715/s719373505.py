n,k = map(int,input().split())
mod = 10**9+7
arr = [0]*(k+1) ##arr[i]はgcdがiの個数
for i in range(k,0,-1):
    l = k//i
    arr[i] = pow(l,n,mod)
    for j in range(2,l+1):
        arr[i] -= arr[i*j]
        arr[i] %= mod
ans = 0
for i,a in enumerate(arr):
    ans+=i*a
    ans%=mod
print(ans) 
