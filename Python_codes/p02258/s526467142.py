N = int(input())

#R[0]
minv = int(input())
maxv = -10**12

#R[1..N-1]
for j in range(1, N):
    r = int(input())
    maxv = max(maxv, r - minv)
    minv = min(minv, r)
    
print(maxv)