from collections import Counter
n=int(input())
a=Counter(map(int,input().split()))
a=sorted(a.items(),key=lambda x:x[0])
l=len(a)

a=[1 if a[i][1]%2==1 else 2 for i in range(l)]
id=[i for i in range(l) if a[i]==2]
l=len(id)

cnt=0
for i in range(l-1):
    if id[i]+1==id[i+1]:
        cnt+=1
        
if cnt==1 and l==2:
    ans=sum(a)-4
else:
    if l%2==0:
        ans=sum(a)-l
    else:
        ans=sum(a)-l-1
print(ans)
