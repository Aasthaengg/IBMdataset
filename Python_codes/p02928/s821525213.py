n,k = map(int,input().split())
a = list(map(int,input().split()))
mod = 10**9+7
X = [0]*n
x = [0]*n
for i in range(n):
    res = 0
    for j in range(i+1,n):
        if a[i] > a[j]:res+=1
    X[i]= res
for i in range(n):
    res = 0
    for j in range(n):
        if a[i] > a[j]:res +=1
    x[i] = res
ans = 0
for i in range(n):
    ans += (k*X[i])%mod+(k*(k-1)*x[i]//2)%mod
    ans %=mod
print(ans)

