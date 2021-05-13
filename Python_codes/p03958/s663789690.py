k,t = map(int, input().split())
a = [int(s) for s in input().split()]

if max(a) <= k / 2:
  print(0)
else:
  print(k - 2*(k-max(a)) - 1)