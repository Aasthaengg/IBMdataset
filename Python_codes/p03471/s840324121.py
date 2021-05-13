n,y=map(int, input().split())
ans=False
for i in range(n+1):
  for j in range(n-i+1):
    if 10000*i+5000*j+1000*(n-i-j)==y:
      ans=True
      x=i
      y=j
      z=n-i-j
if ans:
  print(x,y,z)
else:
  print(-1,-1,-1)