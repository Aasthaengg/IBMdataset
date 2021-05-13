def tickets(a, t):
  # a の最大値をt以下にするのに必要なチケットの枚数を答える
  ret = 0
  for x in a:
    while (x > t):
      x //= 2
      ret += 1
  return ret

def resolve():
  n, m = map(int, input().split())
  a = list(map(int, input().split()))

  lb = -1
  ub = 1000000000
  while (ub - lb > 1):
    mid = lb + (ub - lb) // 2
    t = tickets(a, mid)
    if t < m:
      ub = mid
    else:
      lb = mid

  t = 0
  for i in range(n):
    while (a[i] > ub):
      a[i] //= 2
      t += 1

  a.sort(reverse=True)

  for i in range(min(n, m-t)):
    a[i] //= 2

  print(sum(a))

  return

if __name__ == "__main__":
  resolve()
