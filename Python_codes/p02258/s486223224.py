n = int(input())
r = [int(input()) for x in range(n)]
maxv = -2000000000
minv = r[0]

for i in range(1, n):
    maxv = max(maxv, r[i] - minv)
    minv = min(minv, r[i])

print(maxv)