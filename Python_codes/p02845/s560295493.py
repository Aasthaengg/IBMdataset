N=int(input())
A=list(map(int,input().split()))
l=[[] for _ in range(3)]
ans=1
p=10**9+7
flag=1
for i in range(N):
    cnt=0
    piv=A[i]
    ind=[]
    for j in range(3):
        if len(l[j])==piv:
            cnt=cnt+1
            ind.append(j)
    if len(ind)==0:
        flag=0
        break
    l[ind[0]].append(piv)
    ans=(ans*cnt)%p
    #print(l,ans)
    #input()
if flag==1:
    print(ans%p)
else:
    print(flag)

