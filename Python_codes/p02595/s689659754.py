N,D=[int(i) for i in input().split()]
ans=0
for i in range(N):
  x,y=[int(i) for i in input().split()] 
  if x*x + y*y <= D*D:
      ans += 1
print(ans)
