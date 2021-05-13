N, K = map(int, input().split())
Z = 0
H = 0
for i in range(N):
  if (i+1)%K == 0:
    Z += 1
  if K%2 == 0 and (i+1)%K == K//2:
    H += 1

print(Z**3+H**3)