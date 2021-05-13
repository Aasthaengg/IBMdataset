a=int(input())
b=int(input())
c=int(input())
x=int(input())
ans=0
for ai in range(a+1):
  for bi in range(b+1):
    for ci in range(c+1):
      y=500*ai+100*bi+50*ci
      if x == y:
        ans+=1
      if y>x:
        break
print(ans)