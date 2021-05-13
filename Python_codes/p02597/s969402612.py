N = int(input())
c = input()
W = 0
R = c.count("R")
if N == R or R == 0:
  print("0")
else:
  cnt = N
  for i in range(N):
    if c[i] == "W":
      W = W + 1
    else:
      R = R - 1
    m = max(W, R)
    if m < cnt:
      cnt = m
  print(cnt)