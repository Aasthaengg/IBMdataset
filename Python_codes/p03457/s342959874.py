n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
x=y=t=0
ans='Yes'
for i in range(n):
  c=a[i]
  xy=c[1]+c[2]-(x+y)
  if xy>c[0]-t:
    ans='No'
    break
  else:
    if xy%2!=(c[0]-t)%2:
      ans='No'
      break
    elif abs(c[1]-x)+abs(c[2]-y)>c[0]-t:
      ans='No'
      break
  x=c[1]
  y=c[2]
  t=c[0]
print(ans)