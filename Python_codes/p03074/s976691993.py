from itertools import accumulate

n,k=map(int,input().split())
s=input()

i=0
if s[0]=='1':
    lst=[]
else:
    lst=[0]

while i<n:
    j=i
    cnt=0
    while j<n and s[i]==s[j]:
        cnt+=1
        j+=1
    
    lst.append(cnt)
    i=j

if 2*k+1>=len(lst):
    print(n)
    exit(0)

csum=list(accumulate(lst))
cur=csum[2*k]
ans=cur
for i in range(2,len(lst),2):
    right=min(i+2*k,len(lst)-1)

    ans=max(ans,csum[right]-csum[i-1])

print(ans)
