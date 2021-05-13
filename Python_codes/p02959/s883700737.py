n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(n):
    if B[i] >= A[i]:
        ans += A[i]
        B[i] -= A[i]
        A[i] = 0
        if B[i] >= A[i + 1]:
            ans += A[i + 1]
            A[i + 1] = 0
        elif B[i] < A[i + 1]:
            ans += B[i]
            A[i + 1] -= B[i]
    elif B[i] < A[i]:
        ans += B[i]
        A[i] -= B[i]

print(ans)
