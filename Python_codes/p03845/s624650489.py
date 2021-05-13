n=int(input())
t=list(map(int,input().split()))
ans=[]
s=sum(t)
m=int(input())
for i in range(m):
    p,x=map(int,input().split())
    ans.append(s-t[p-1]+x)
for i in range(m):
    print(ans[i])
