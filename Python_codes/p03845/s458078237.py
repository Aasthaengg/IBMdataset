n=int(input())
t=list(map(int,input().split()))
m=int(input())
ans=[0]*m
for i in range(m):
    p,x=map(int,input().split())
    ans[i]=sum(t)-t[p-1]+x
for i in range(m):
    print(ans[i])