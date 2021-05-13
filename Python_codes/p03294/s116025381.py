def gcd(x, y):
  if y != 0:
    return gcd(y, x % y)
  else:
    return x

def lcm(x, y):
  return (x // gcd(x, y)) * y

def calc(a, m):
  ans = 0
  for x in a:
    ans += m % x
  return ans

def resolve():
  n = int(input())
  a = list(map(int, input().split()))
  m = 1
  for i in range(n):
    m = lcm(a[i], m)
  m -= 1
  ans = calc(a, m)
  print(ans)
  return

if __name__ == "__main__":
  resolve()
