A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
XYC = [list(map(int, input().split())) for m in range(M)]
ans = min(a)+min(b)
for m in range(M):
  tmp = a[XYC[m][0]-1]+b[XYC[m][1]-1]-XYC[m][2]
  ans = min(tmp, ans)
print(ans)