n,k = map(int, input().split())

mod = 10**9+7
cnts=[0]*(k+1)

for x in reversed(range(1,k+1)):
    num= k//x

    c = pow(num,n,mod)
    for j in range(2,num+1):
        c-= cnts[x*j]
    cnts[x]=c

ans=0
for i in range(1,k+1):
    ans+=(i*cnts[i])
print(ans%mod)