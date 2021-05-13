n=int(input())
x=[0,0,0]
ans="Yes"
for i in range(n):
  y=x
  x=list(map(int,input().split()))
  if x[0]-y[0]<abs(y[1]-x[1])+abs(y[2]-x[2]) or (x[1]+x[2])%2!=x[0]%2:
    ans="No"
    break
print(ans)
