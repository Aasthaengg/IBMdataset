N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]
I = [1] * N

ans = X

for j in range(1, D + 1):
    for i in range(N):
        if I[i] == j:
            ans += 1
            I[i] += A[i]

print(ans)
