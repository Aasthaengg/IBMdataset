import math

n,_,*a=map(int,open(0).read().split())
match={1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
a=sorted(a)

num=[0]*8

for d in a:
    num[match[d]]=d

dig=set(num)
dig.remove(0)
dig=sorted(list(dig),reverse=True)

dp=[-10**10]*(n+1)
dp[0]=0

for i in range(n+1):
    for d in dig:
        if i-match[d]<0:
            continue

        dp[i]=max(dp[i],dp[i-match[d]]+1)

ans=''

i=n
while i>0:
    for d in dig:
        if i-match[d]<0:
            continue
        if dp[i]==dp[i-match[d]]+1:
            ans=ans+str(d)
            break
    
    i-=match[d]

print(ans)