n, k = map(int, input().split())
A = list(map(int, input().split()))
d = 10**9 + 7

down1 = 0
for i in range(n-1):
  for j in range(i+1, n):
    if A[i] > A[j]: down1 += 1

down2 = 0
for i in range(n):
  for j in range(n):
    if A[i] > A[j]: down2 += 1

ans = (down2 * ((k-1) * k // 2)) % d
ans = (ans + down1 * k) % d
print(ans)