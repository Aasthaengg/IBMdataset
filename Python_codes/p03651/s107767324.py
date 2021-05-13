def gcd(x, y):
  if y == 0:
    return x
  else:
    return gcd(y, x % y)

def resolve():
  n, k = map(int, input().split())
  a = list(map(int, input().split()))
  if k in a:
    print('POSSIBLE')
    return

  if k > max(a):
    print('IMPOSSIBLE')
    return

  g = a[0]
  for x in a:
    g = gcd(x, g)

  for x in a:
    if x < k:
      continue
    if (x - k) % g == 0:
      print('POSSIBLE')
      return

  print('IMPOSSIBLE')
  return

if __name__ == "__main__":
  resolve()
