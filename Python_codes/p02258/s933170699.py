R = [int(input()) for i in range(int(input()))]
maxp = R[1] - R[0]
minv = R[0]
for r in R[1:]:
    maxp = max(maxp, r-minv)
    minv = min(minv, r)
print(maxp)