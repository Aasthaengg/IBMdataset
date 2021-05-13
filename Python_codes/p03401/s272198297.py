n = int(input())
a = [0]
a += list(map(int, input().split()))
a.append(0)
d = []
for i in range(n + 1):
  d.append(abs(a[i] - a[i + 1]))
s = sum(d)
for i in range(n):
  print(s - d[i] - d[i + 1] + abs(a[i] - a[i + 2]))