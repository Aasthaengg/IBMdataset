N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0

for i in range(1, N):
    A[i] = A[i - 1] + A[i]
    if A[i] > K:
        A = A[:i]
        break
A = [0] + A
A = A[::-1]

for i in range(1, M):
    B[i] = B[i - 1] + B[i]
    if B[i] > K:
        B = B[:i]
        break
B = [0] + B

A_length = len(A)
B_length = len(B)

j = 0
for i in range(A_length):

    while j < B_length:
        if A[i] + B[j] <= K:
            j += 1
        else:
            break
    j -= 1

    ans = max(ans, A_length - (i + 1) + j)
print(ans)
