X = list(map(int,input().split()))
N = X[0]
M = X[1]
C = int(X[2])
B = list(map(int,input().split()))
A = [input().split() for l in range(N)]


correct = 0
for N_iter in range(N):
    line_sum = 0
    for M_iter in range(M):
        line_sum += int(A[N_iter][M_iter])*B[M_iter]
    line_sum += C
    if line_sum > 0:
        correct += 1

print(correct)