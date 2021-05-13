N = int(input())
V = list(map(int,input().split()))
C = list(map(int,input().split()))

out=0
XY = [0]*N
for i in range(N):
    XY[i] = V[i] - C[i]
    if XY[i]>0:
        out+=XY[i]

print(out)