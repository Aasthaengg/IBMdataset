import sys
readline = sys.stdin.readline

N,H = map(int,readline().split())
maxA = 0
B = [0] * N
for i in range(N):
  a,b = map(int,readline().split())
  B[i] = b
  if maxA < a:
    maxA = a

usefulB = []
for i in range(N):
  if B[i] > maxA:
    usefulB += [B[i]]

usefulB = sorted(usefulB,reverse = True)

cnt = 0
for b in usefulB:
  H -= b
  cnt += 1
  if H <= 0:
    print(cnt)
    break
else:
  cnt += (H + maxA - 1) // maxA
  print(cnt)