N = int(input())
T,A = (int(X) for X in input().split())
H = [int(X) for X in input().split()]
MIN = pow(10,9)
MII = 0
for X in range(0,N):
    Diff = abs(A-(T-0.006*H[X]))
    if Diff<MIN:
        MIN = Diff
        MII = X+1
print(MII)