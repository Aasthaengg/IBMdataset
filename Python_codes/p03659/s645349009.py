n = int(input())
a = list(map(int, input().split()))
total = sum(a)
b = 0
arr = []
ans = 0
for i in range(n - 1):
  b += a[i]
  c = total - b
  arr.append(abs(b - c))
  if abs(b - c) == 0:
    break
ans = min(arr)
print(ans)