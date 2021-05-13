a,b=map(int,input().split())
ans=0
if (a-b)%2!=0:
    ans="IMPOSSIBLE"
else:
    ans=int((a+b)/2)
print(ans)