N = int(input())
ans = 10**5

def base(x, n):
  A = 0
  while x != 0:
    A += x % abs(n)
    if n < 0:
      x = - ( (-x)//n )
    else:
      x //= n
  return A

for i in range(N+1):
  ans = min(ans, base(i, 6) + base(N-i, 9))

print(ans)