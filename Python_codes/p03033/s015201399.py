from bisect import bisect_left as bl
N, Q = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
X.sort(key = lambda x: x[2])
Y = [int(input()) for _ in range(Q)]
res = [-1] * Q
jump = [-1] * Q
for s,t,x in X:
  l=bl(Y,s - x)
  r=bl(Y,t - x)
  while l < r:
    s = jump[l]
    if s == -1:
      res[l] = x
      jump[l] = r
      l += 1
    else:
      l = s
print(*res,sep = '\n')