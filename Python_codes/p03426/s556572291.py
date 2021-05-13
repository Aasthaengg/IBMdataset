h,w,d=map(int,input().split())
num=[0]*(h*w)
for i in range(h):
    a=list(map(int,input().split()))
    for j in range(w):
        num[a[j]-1]=(i,j)

cost=[0]*(h*w)
for i in range(d,h*w):
    cost[i]=cost[i-d]+abs(num[i][0]-num[i-d][0])+abs(num[i][1]-num[i-d][1])

q=int(input())
ans=[0]*q
for i in range(q):
    l,r=map(int,input().split())
    ans[i]=cost[r-1]-cost[l-1]

print(*ans,sep='\n')