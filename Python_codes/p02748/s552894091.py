A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
xyc = [list(map(int, input().split())) for _ in range(M)]
ans = 0
lpr = min(a) + min(b)
dcp = []

for i in range(M):
    indexA = xyc[i][0] - 1
    indexB = xyc[i][1] - 1
    dcp.append(a[indexA] + b[indexB] - xyc[i][2])

ans = min(min(dcp), lpr)
print(ans)