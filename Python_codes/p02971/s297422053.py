import sys
def I(): return int(sys.stdin.readline().rstrip())


N = I()
A = [I() for _ in range(N)]

B = [0]*N  # Bi = A1~Aiまでのmax
C = [0]*N  # Ci = Ai~ANまでのmax
for i in range(N):
    if i == 0:
        B[i] = A[i]
    else:
        B[i] = max(B[i-1],A[i])
for i in range(N-1,-1,-1):
    if i == N-1:
        C[i] = A[-1]
    else:
        C[i] = max(C[i+1],A[i])

for i in range(N):
    if i == 0:
        print(C[1])
    elif i == N-1:
        print(B[-2])
    else:
        print(max(B[i-1],C[i+1]))
