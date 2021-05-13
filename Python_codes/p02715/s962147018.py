mod=10**9+7
n,k= map(int, input().split())
x=[0]*(k+1)
y=0

# 最大公約数がその数になる組合せで場合わけ、後ろから埋めて重複を引く
for i in range(k,0,-1):
    m=k//i
    x[i]=pow(k//i,n,mod)
    for j in range(1,m):
        x[i]-=x[i*(j+1)]
        x[i]%=mod

ans=0
for i in range(1,k+1):
    ans+=x[i]*i
    ans%=mod

print(ans)