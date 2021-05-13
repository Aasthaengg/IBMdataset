n=int(input())
L=list(map(int,input().split()))
ans=0
ans+=min(L)
for i in range(n):
    L[i]-=ans
L=[0]+L+[0]
while True:
    tmp=0
    for i in range(1,n+2):
        if L[i]==0 and len(L[tmp:i])!=0:
            if len(L[tmp:i])==1:
                Min=L[tmp+1]
            else:
                Min=min(L[tmp+1:i])
            ans+=Min
            for j in range(tmp+1,i):
                L[j]-=Min
            tmp=i
    if max(L)==0:
        break
print(ans)