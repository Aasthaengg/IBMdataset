N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(N-1, -1, -1):
    if B[i] >= A[i+1]:
        B[i] -= A[i+1]
        ans += A[i+1]
        A[i+1] = 0
        if B[i] >= A[i]:
            ans += A[i]
            A[i] = 0
        else:
            ans += B[i]
            A[i] -= B[i]
    else:
        ans += B[i]
print(ans)