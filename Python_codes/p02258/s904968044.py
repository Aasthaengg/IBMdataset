n = input()
R = [0 for i in range(n)]
for i in range(n):
    R[i] = input()
maxv = -2000000000
minv = R[0]

for j in range(1, n):
    maxv = max(maxv, R[j] - minv)
    minv = min(minv, R[j])

print maxv