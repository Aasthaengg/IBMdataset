N = int(input())
ans = [0]*N
for x in range(1, int(N**0.5)+2):
  for y in range(1, int(N**0.5)+2):
    for z in range(1, int(N**0.5)+2):
      a = x**2 + y**2 + z**2 + x*y + y*z + z*x 
      if a <= N:
        ans[a-1] += 1
for i in range(N):
  print(ans[i])