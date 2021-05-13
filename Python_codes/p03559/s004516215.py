N=int(input())
la=list(map(lambda x:[int(x),0],input().split()))
lb=list(map(lambda x:[int(x),1],input().split()))
lc=list(map(lambda x:[int(x),2],input().split()))
l=la+lb+lc
l.sort(key=lambda x:(x[0],-x[1]))
na=0
sumb=0
ans=0
for i in range(3*N):
    if l[i][1]==0:
        na+=1
    elif l[i][1]==1:
        sumb+=na
    else:
        ans+=sumb
print(ans)
