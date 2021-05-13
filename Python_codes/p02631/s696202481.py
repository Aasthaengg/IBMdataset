n = int(input())
a = list(map(int, input().split()))
s = 0
for i in range(n):
  s = s ^ a[i]
b = [0] * n
for i in range(n):
  b[i] = s ^ a[i]

print(*b)