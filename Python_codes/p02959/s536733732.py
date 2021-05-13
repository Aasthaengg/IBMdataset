n=int(input())
alist=list(map(int,input().split()))
blist=list(map(int,input().split()))
ini=sum(alist)

for i in range(n):
    tmpa=alist[i]
    tmpb=blist[i]
    if tmpb >=tmpa:
        alist[i]=0
        tmpb-=tmpa
        alist[i+1]=max(0,alist[i+1]-tmpb)
    else:
        alist[i]-=tmpb
print(ini-sum(alist))