n,m=map(int,input().split())
from collections import defaultdict
a=list(map(int,input().split()))
dic={i:[2,5,5,4,5,6,3,7,6][i-1]for i in range(1,10)}
s={}
for i in a:
    if dic[i] in s:
        s[dic[i]]=max(s[dic[i]],i)
    else:
        s[dic[i]]=i
ok=list(s.items())#hon,digit
dp=[-float('inf')]*(n+1)
dp[0]=0
for i in range(1,n+1):
    for h,d in ok:
        if h<=i:
            dp[i]=max(dp[i],dp[i-h]+1)
from operator import itemgetter as it 
ok.sort(reverse=1,key=it(1))
ans=''
now=n
keta=dp[n]
while keta>1:
    for h,d in ok:
        if now>h and dp[now]==dp[now-h]+1:
            ans+=str(d);now-=h;keta-=1;break
print(ans+str(s[now]))