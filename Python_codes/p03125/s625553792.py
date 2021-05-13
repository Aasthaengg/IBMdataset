n, m = map(int, input().split())

if m % n == 0:
    print(n + m)
else:
  print(m - n)