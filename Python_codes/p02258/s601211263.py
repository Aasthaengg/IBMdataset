n = input()
R = []
for i in range(n):
    R.append(input())

maxv = R[1] - R[0]
minv = R[0]
for j in range(1, n):
    maxv = max(maxv, R[j] - minv)
    minv = min(minv, R[j])

print "%d" % maxv