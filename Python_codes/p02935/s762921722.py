n=int(input())
v=list(map(int,input().split()))
v.sort(reverse=True)

ans=v.pop()
for i in range(n-1):
  tt=v.pop()
  ans=(ans+tt)/2
print(ans)
