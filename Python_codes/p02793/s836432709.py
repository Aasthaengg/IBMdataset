n = int(input())
a = [int(x) for x in input().split()]
mod = 10**9+7
res = [0]*(max(a)+1)
ma = 0
for i in a:
    for j in range(2,int(i**0.5)+1):
        cnt = 0
        while i%j==0:
            i//=j
            cnt+=1
        res[j] = max(res[j],cnt)
    if i!=1:
        res[i] = max(res[i],1)

d = 1
for i in range(max(a)+1):
    if res[i]>0:
        d=d*i**res[i]%mod
ans = 0
for i in range(n):
    m = pow(a[i],mod-2,mod)
    ans = (ans+(d*m)%mod)%mod
print(ans)