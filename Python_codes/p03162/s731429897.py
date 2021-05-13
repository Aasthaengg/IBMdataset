n = int(input())
p = [list(map(int, input().split())) for i in range(n)]

dpa, dpb, dpc = [0]*(n+1), [0]*(n+1), [0]*(n+1)
dpa[0] = dpb[0] = dpc[0] = 0

for i in range(n):
    dpa[i + 1] = max(dpb[i] + p[i][0], dpc[i] + p[i][0])
    dpb[i + 1] = max(dpc[i] + p[i][1], dpa[i] + p[i][1])
    dpc[i + 1] = max(dpa[i] + p[i][2], dpb[i] + p[i][2])

print(max(dpa[n], dpb[n], dpc[n]))