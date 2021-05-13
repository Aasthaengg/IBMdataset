K, N = map(int, input().split())
A = sorted(map(int, input().split()))
assert len(A) == N


dists = []
for i,start in enumerate(A):
  # 右回り
  posR = A[(i - 1) % N] + (K if A[(i - 1) % N] < start else 0)
  #max([a + K for a in A[:i]] + A[i+1:])
  # 左回り
  posL = A[(i + 1) % N] - (K if A[(i + 1) % N] > start else 0)
  #posL = min(A[:i] + [a - K for a in A[i+1:]])
#  print(start, posL, posR)
  dists.append(min(posR - start, - posL + start))
#print(dists)
print(min(dists))