n = int(input())
k = int((n * 2) ** 0.5)
while True:
  p = (k+1) * k // 2
  if p >= n: break
  k += 1
diff = abs(n - p)
for i in range(1, k+1):
  if i != diff: print(i)