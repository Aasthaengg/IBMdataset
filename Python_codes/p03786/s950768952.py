import bisect
n=int(input())
a=list(map(int,input().split()))
a.sort()
#print(a)
x=bisect.bisect_left(a,a[-1]/2)
#print(x)
ans=n-x#そのままの状態で条件を満たす和
if x==0:
    print(ans)
    exit()
i=x-1
j=x
tmp=a[i]
ref=a[x]
SUM=sum(a[:i+1])
#print(SUM)
for k in range(i,-1,-1):
    if k==i:
        if 2*SUM>=a[k+1]:
            ans+=1
        else:
            break
    else:
        SUM-=a[k+1]
        #print(SUM,k,ans)
        if 2*SUM>=a[k+1]:
            ans+=1
        else:
            break
print(ans)