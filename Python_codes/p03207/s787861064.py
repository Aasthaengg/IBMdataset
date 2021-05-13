N = int(input())
M = 0
P = 0
for i in range(N):
    A = int(input())
    P += A
    M = max(M,A)

print(P - M//2)