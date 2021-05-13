n=int(input())
a=list(map(int,input().split()))
a_=max(a)
con=[0]*(a_+1)
tou=[0]*(a_+1)
ans=[]
for i in range(len(a)):
    u=a[i]
    if u==0:
        con[0]+=1
        tou[0]+=1
        ans.append(4-con[0])

    else:
        con[u]+=1 
        tou[u]+=1  
        ans.append(tou[u-1]-con[u]+1)
c=1
for i in range(len(ans)):
    c*=ans[i]
    c=c%(10**9+7)
print(c%(10**9+7))   

