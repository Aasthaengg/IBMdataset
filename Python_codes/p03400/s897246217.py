n = int(input())
d, x = map(int, input().split())
a = [int(input()) for _ in range(n)]
total = 0
for i in range(len(a)):
  eat = 0
  count = 0
  while eat <= d:
    count += 1
    eat = a[i] * count + 1
  total += count
print(total + x)