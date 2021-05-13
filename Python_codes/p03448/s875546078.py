a = int(input())
b = int(input())
c = int(input())
x = int(input())
ans = []

for i in range(a + 1):
  total = 0
  for j in range(b + 1):
    for k in range(c + 1):
      total = 500 * i + 100 * j + 50 * k
      if x == total:
        ans.append((i, j, k))
print(len(ans))