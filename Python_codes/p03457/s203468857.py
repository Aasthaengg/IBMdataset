n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
x=y=t=0
ans='Yes'
for i in range(n):
  xy=a[i][1]+a[i][2]-(x+y)
  if xy>a[i][0]-t:
    ans='No'
    break
  else:
    if xy%2!=(a[i][0]-t)%2:
      ans='No'
      break
    elif abs(a[i][1]-x)+abs(a[i][2]-y)>a[i][0]-t:
      ans='No'
      break
  x=a[i][1]
  y=a[i][2]
  t=a[i][0]
print(ans)