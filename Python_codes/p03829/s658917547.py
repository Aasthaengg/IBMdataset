N, A, B = map(int,input().split())
XN = list(map(int,input().split()))

ans = 0
for n in range(N-1):
  xl = XN[n]
  xr = XN[n+1]
  dist = xr - xl
  ans += min(dist*A, B)
print(ans)
