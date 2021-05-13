N = int(input())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))
C = [0] + list(map(int, input().split()))
ans = 0
for i in range(1, N + 1):
    ans += B[A[i]]
    if i >= 2 and A[i - 1] + 1 == A[i]:
        ans += C[A[i - 1]]
print(ans)
