N = int(input())
R = [int(input()) for i in range(N)]

maxv = R[1] - R[0]
minv = R[0]
for i in range(1,len(R)):
    maxv = max(maxv,R[i]-minv)
    minv = min(minv,R[i])

print (maxv)