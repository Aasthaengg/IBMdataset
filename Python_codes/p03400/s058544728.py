n = int(input())
d, x = map(int, input().split())

count = 0
for i in range(n):
  a = int(input())
  count += len([j for j in range(1, d + 1, a)])
print(count + x)