N, K = list(map(int, input().split()))
L = list(map(int, input().split()))

L = sorted(L, reverse=True)

total = 0
for k in range(K):
  total += L[k]
  
print(total)