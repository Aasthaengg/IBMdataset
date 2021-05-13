n=int(input())
t=list(map(int,input().split()))
m=int(input())
ans=[0]*m

for i in range(1,m+1):
    total=0
    p,x=map(int,input().split())
    for j in range(1,n+1):
        if j==p:
            total+=x
        else:
            total+=t[j-1]
    
    else:
        ans[i-1]+=total

for i in ans:
    print(i)