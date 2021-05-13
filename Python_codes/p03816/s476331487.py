from collections import Counter
N=int(input())
A=sorted(map(int,input().split()))
li=[]
i=0
while(i<N):
    cnt=0
    j=i
    while(j<N and A[i]==A[j]):
        cnt+=1
        j+=1
    li.append(cnt-1)
    i=j
l=len(li)
for i in range(l):
    for j in range(i+1,l):
        if li[i]==0:
            break
        d=min(li[i],li[j])
        li[i]-=d
        li[j]-=d
for i in range(l):
    li[i]%=2
ans=len(set(A))
for i in range(l):
    ans-=li[i]
print(ans)