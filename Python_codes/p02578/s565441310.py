N = int(input())
A = list(map(int, input().split()))

ans = A[0]
a = A[0]

for i in range(1, N):
    ans += max(A[i], a)
    a = max(A[i], a)

print(ans - sum(A))