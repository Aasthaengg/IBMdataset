N = int(input())
B = list(map(int, input().split()))
A = [0]*N
Bp = 1<<100
for i in range(N-1):
    A[i] = min(B[i], Bp)
    Bp = B[i]
A[N-1] = B[N-2]
print(sum(A))