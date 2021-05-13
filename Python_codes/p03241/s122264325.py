def divisor(n):
  cd = []
  i = 1
  while i*i <= n:
    if n%i==0:
      cd.append(i)
      if i != n//i:
        cd.append(n//i)
    i += 1
  return cd

def solve():
  N, M = map(int, input().split())
  cd = divisor(M)
  cd.sort()
  for c in cd:
    if c<=M//N:
      ans = c
  return ans
print(solve())