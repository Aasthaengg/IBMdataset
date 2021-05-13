def solve():
  N = int(input())
  ans = [0]*N
  for x in range(1,101):
    for y in range(1,101):
      for z in range(1,101):
        p = x*x + y*y + z*z + x*y + y*z + z*x
        if p <= N:
          ans[p-1] += 1
  return ans
print(*solve(),sep='\n')
