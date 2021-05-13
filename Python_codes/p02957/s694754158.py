a,b=map(int,input().split())
ans="IMPOSSIBLE"
if a%2==b%2:
    ans=int((a+b)/2)
print(ans)