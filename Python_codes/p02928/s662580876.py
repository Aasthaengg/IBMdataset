from collections import Counter
N,K = list(map(int, input().split()))
A = list(map(int, input().split()))
mod = int(1e9+7)

cnt1 = 0
for i in range(N):
  for j in range(i+1,N):
    if A[i] > A[j]:
      cnt1 += 1

cnt2 = 0
for i in range(N):
  for j in range(N):
    if A[i] > A[j]:
      cnt2 += 1
    
print((cnt1 * K % mod + ((cnt2 * K * (K-1)) ) // 2 ) % mod)