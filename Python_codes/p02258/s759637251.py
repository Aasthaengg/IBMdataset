n = int(input())
R = [0]*n
for i in range(n):
    R[i] = int(input())
    
minv = R[0]
maxv = R[1] - R[0]
for i in range(1,n):
    maxv = max(maxv, R[i] - minv)
    minv = min(minv, R[i])
print(maxv)
