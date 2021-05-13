N = int(input())
A = [0] * N
B = list(map(int, input().split()))
for i in range(N):
    if i == 0:
        A[i] = B[i]
    elif i == (N - 1):
        A[i] = B[i - 1]
    else:
        A[i] = min(B[i - 1], B[i])
print(sum(A))
