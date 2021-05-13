N, M = map(int, input().split())
maxL = 0
minR = N-1
LR = [0, N-1]
for i in range(M):
  LR = [int(i)-1 for i in input().split()]
  maxL = max(maxL, LR[0])
  minR = min(minR, LR[1])
if minR-maxL>=0:
  print(minR-maxL+1)
else:
  print(0)
