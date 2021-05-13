N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

totalA = [0]
totalB = [0]
sumA = 0
for i in range(N):
    sumA += A[i]
    totalA.append(sumA)
sumB = 0
for i in range(M):
    sumB += B[i]
    totalB.append(sumB)

iB = M
countMax = 0
for iA in range(N+1):
  if totalA[iA]>K:
    break
  else:
    while totalA[iA] + totalB[iB] > K:
      iB -= 1
  countMax = max(countMax,iA+iB)

print(countMax)

