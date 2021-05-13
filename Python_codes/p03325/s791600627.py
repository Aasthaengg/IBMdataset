n = int(input())
a = list(map(int, input().split()))
total = 0
for i in range(n):
  cnt = 0
  while True:
    if a[i] % 2 == 0:
      cnt += 1
      a[i] = a[i] // 2
    else:
      break
  total += cnt
print(total)