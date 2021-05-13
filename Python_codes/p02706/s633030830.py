n, m = map(int, input().split())
lst = [int(i) for i in input().split()]

for i in range(m):
  n -= lst[i]
  if n < 0:
    n = -1
    break

print(n)