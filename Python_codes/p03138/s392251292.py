import math

N, K  = map(int, input().split())
A = list(map(int, input().split()))

B = [[0] * 2 for _ in range(40)]

for i in range(N):
  Ai = A[i]
  for j in range(40):
    if Ai % 2 == 0:
      B[j][0] += 1
    else :
      B[j][1] += 1
    Ai = Ai // 2
    #print(B)

Xmax = 0
if K != 0:

  Kd = int(math.log2(K))+1

  for i in range(Kd-1,-1,-1):
    if B[i][0] > B[i][1]:
      Xmax += 2**i
      if Xmax > K:
        Xmax -= 2**i
    
ans = 0
for i in range(N):
  ans += Xmax ^ A[i]

print(ans)