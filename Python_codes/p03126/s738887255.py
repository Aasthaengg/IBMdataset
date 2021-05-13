n,m=map(int,input().split())
ans=list(map(int,input().split()))
ans=set(ans[1:])
for i in range(n-1):
    t=list(map(int,input().split()))
    t=set(t[1:])
    ans=ans&t
print(len(ans))