n = int(input())
A, B, C = [[int(x) for x in input().split()] for _ in range(3)]

ans = 0
for i in range(n):
    ans += B[A[i] - 1]

for i in range(n - 1):
    if A[i + 1] - A[i] == 1:
        ans += C[A[i] - 1]

print(ans)
