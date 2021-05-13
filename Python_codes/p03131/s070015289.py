k,a,b = map(int, input().split())
res = 1
if b <= a + 1:
  print(res + k)
else:
  if k < a - 1 + 2:
    print(res + k)
  else:
    res += b - 1
    k -= a + 1
    print(res + k//2 * (b - a) + k % 2)