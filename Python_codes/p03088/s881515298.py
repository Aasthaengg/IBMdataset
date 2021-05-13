n=int(input())
d={}
drev={}
a=["A","C","G","T"]
judge=["AGC","ACG","GAC"]
ans=[[1 for i in range(61)]]+[[0 for i in range(61)] for j in range(n-3)]
cnt=0
mod=10**9+7
for i in range(4):
    for j in range(4):
        for k in range(4):
            s=a[i]+a[j]+a[k]
            if s == "AGC" or s =="ACG" or s == "GAC":continue
            d[s]=cnt
            drev[cnt]=s
            cnt+=1
for i in range(1,n-2):
    for j in range(61):
        for k in range(4):
            h=drev[j]+a[k]
            if h[1:] in judge or h[0]+h[2:]=="AGC" or h[:2]+h[3]=="AGC":continue
            ans[i][d[h[1:]]]+=ans[i-1][j]
            ans[i][d[h[1:]]]%=mod
print(sum(ans[-1])%mod)