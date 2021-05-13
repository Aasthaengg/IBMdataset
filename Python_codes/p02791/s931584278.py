N=int(input())
P=list(map(int,input().split()))
ans=0
min=P[0]
for i in P:
    if i==1:
        ans+=1
        break
    if min>=i:
        min=i
        ans+=1
print(ans)
