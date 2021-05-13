n,m=map(int,input().split())
a=list(map(int,input().split()))
from collections import Counter
cc=Counter()
cc[0]=1
su=0
ans=0
for i in a:
    su+=i
    su%=m
    ans+=cc[su]
    cc[su]+=1
print(ans)
