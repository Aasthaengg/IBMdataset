N, T = map(int, input().split())
arrc = []
arrt = []

for i in range(1,N+1):
  c, t = map(int, input().split())
  arrc.append(c)
  arrt.append(t)

if min(arrt) > T:
  print("TLE")
else:
  ans = arrc[0]
  for i in range(0,N):
    if arrt[i] <= T:
      if arrc[i] < ans:
        ans = arrc[i]
  print(ans)