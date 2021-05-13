N = int(input())
a = [0]
a += list(map(int, input().split(' ')))
b = [0 for _ in range(N + 10)]
for i in range(N, 0, -1):
  res = 0
  for j in range(N // i * i, i, -i):
    res = res ^ b[j]
  b[i] = res ^ a[i]
print(sum(b))
for i in range(1, N + 1):
  if b[i]:
    print(i)