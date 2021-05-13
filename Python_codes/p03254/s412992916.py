n, x = map(int, input().split())
lst = [0] + sorted(list(map(int, input().split())))
for i in range(n):
  lst[i + 1] += lst[i]
for i in range(n):
  if lst[i] <= x < lst[i + 1]:
    print(i)
    exit()
if x == lst[n]:
  print(n)
else:
  print(n - 1)