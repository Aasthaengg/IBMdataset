N = int(input())
A = list(map(int,input().split()))
A = sorted(A)[::-1]
S = 0
for i in range(2*N):
    if i % 2 == 1:
        S += A[i]
print(S)
