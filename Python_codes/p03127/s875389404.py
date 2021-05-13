def gcd(x, y):
  if y == 0:
    return x
  else:
    return gcd(y, x % y)

def resolve():
  n = int(input())
  a = list(map(int, input().split()))
  ans = a[0]
  for x in a:
    ans = gcd(ans, x)

  print(ans)
  return

if __name__ == "__main__":
  resolve()
