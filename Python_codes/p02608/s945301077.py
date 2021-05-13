def solve():
  N = int(input())
  ans = [0]*(N+1)
  for x in range(1,100):
    for y in range(1,100):
      for z in range(1,100):
        left = x*x+y*y+z*z+x*y+y*z+z*x
        if left<=N:
          ans[left] += 1
  return ans[1:]
print(*solve(),sep='\n')