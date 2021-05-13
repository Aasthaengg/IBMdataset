A,B,M = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))
XYC = [list(map(int,input().split())) for _ in range(M)]
MIN = min(A)+min(B)
for xyc in XYC:
    MIN = min(MIN,A[xyc[0]-1]+B[xyc[1]-1]-xyc[2])
print(MIN)