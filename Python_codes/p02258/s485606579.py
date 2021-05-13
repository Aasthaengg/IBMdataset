N = int(input())
R = [int(input()) for i in list(range(N))]
maxv = -1000000000
minr = R[0]

for i in list(range(1, N)):
    maxv = max(maxv, R[i] - minr)
    minr = min(minr, R[i])

print(maxv)