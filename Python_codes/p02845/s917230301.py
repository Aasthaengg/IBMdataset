N=int(input())
A=list(map(int,input().split()))
mod=10**9+7

dp=[1]
col=[]
for i in range(N):
    if A[i]==0:
        col.append(1)
        dp.append(dp[-1]*(4-len(col)))
    else:
        p=0
        for c in range(len(col)):
            if col[c]==A[i]:
                p+=1
                if p==1:
                    col[c]+=1
        dp.append(dp[-1]*p%mod)

print(dp[-1]%mod)
