l,r=map(int, input().split())
if l//673 != r//673 and l//3 != r//3:
  print(0)
else:
  ans=2019**2
  for i in range(l,r):
    for j in range(i+1,r+1):
      if (i*j)%2019 < ans:
        ans = (i*j)%2019
  print(ans)