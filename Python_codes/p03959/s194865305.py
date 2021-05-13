n=int(input())
tM=list(map(int,input().split()))
aM=list(map(int,input().split()))
tm=[1]*n
am=[1]*n

tm[0]=tM[0]
for i in range(1,n):
    if tM[i]>tM[i-1]:
        tm[i]=tM[i]

aM.reverse()
am[0]=aM[0]
for i in range(1,n):
    if aM[i]>aM[i-1]:
        am[i]=aM[i]
aM.reverse()
am.reverse()

m=[]
M=[]
for i in range(n):
    m.append(max(tm[i],am[i]))
    M.append(min(tM[i],aM[i]))

ans=1
mod=10**9+7
for i in range(n):
    ans*=max(0,M[i]-m[i]+1)
    ans%=mod

print(ans)
