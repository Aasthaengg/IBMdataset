n, k = map(int, input().split())
a = sorted([(list(map(int, input().split()))) for i in range(n)])
i = 0

while True:
  if (k - a[i][1]) > 0:
    k -= a[i][1]
    i += 1
  else:
    print(a[i][0])
    break