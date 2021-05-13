N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

D = [0] * N
for i in range(N):
  D[i] = A[i] - B[i]
  
if sum(D) < 0:
  print(-1)
  exit(0)

D.sort()
  
minsum = 0
minidx, maxidx = 0, 0
cumsumR = [0] * (N+1)

for i in range(N):
  if D[i] >= 0:
    minidx = i
    break
  minsum += D[i]
  
for j in range(N-1,-1,-1):
  if minsum >= 0:
    maxidx = j
    break
  minsum += D[j]
  
print(N - (maxidx - minidx + 1))