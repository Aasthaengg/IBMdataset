n,m=map(int,input().split())
mylist=[n]*m
for i in range(n):
    ans=list(map(int,input().split()))
    for j in range(1,ans[0]+1):
        mylist[ans[j]-1]-=1
print(mylist.count(0))