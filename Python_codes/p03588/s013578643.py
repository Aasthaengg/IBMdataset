n=int(input())
mx=0
ans=0

for i in range(n):
  a,b=map(int,input().split())
  if a>mx:
    mx=a
    ans=a+b
print(ans)