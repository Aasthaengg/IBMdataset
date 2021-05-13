def gcd(x, y):
  if y != 0:
    return gcd(y, x % y)
  else:
    return x

def lcm(x, y):
  return (x // gcd(x, y)) * y



def resolve():
  n = int(input())
  t = []
  for i in range(n):
    t.append(int(input()))
  ans = 1
  for x in t:
    ans = lcm(x, ans)

  print(ans)
  return

if __name__ == "__main__":
  resolve()
