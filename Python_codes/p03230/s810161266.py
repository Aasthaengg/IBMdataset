n = int(input())
k = int((n*2)**.5) + 1

if (k - 1) * k / 2 == n:
  print('Yes')
  print(k)
else:
  print('No')
  exit()

t = [1] * (k - 1)

for i in range(1, k - 1):
  t[i] = t[i-1] + i

for i in range(k-1):
  s = (t[max(i, j)] + min(i, j) for j in range(k-1))
  print(k-1, *s)
print(k - 1, *(t[j] + j for j in range(k-1)))