MOD=10**9+7
n=int(input())
la=list(map(int,input().split()))
lb=list(map(int,input().split()))
l=[[1,10**9] for i in range(n)]
tmp=0
for num,i in enumerate(la):
    if i>tmp:
        l[num][0]=i
        l[num][1]=i
    else :
        l[num][1]=i
    tmp=max(tmp,i)
tmp=0
ans=1
for i in range(n-1,-1,-1):
    if lb[i]<l[i][0]:
        print(0);exit()
    elif lb[i]>tmp:
        if lb[i]<=l[i][1]:ans*=1 
        else:print(0);exit()
    else:
        ans=ans*(min(lb[i],l[i][1])-l[i][0]+1)%MOD
    tmp=max(tmp,lb[i])
print(ans)