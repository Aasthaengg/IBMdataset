N = int(input())
A = [0] + list(map(int, input().split())) + [0]
pre = 0
yen = sum(abs(i - j) for i, j in zip(A, A[1:]))
ans = [yen] * N
for i in range(N):
    ans[i] += -abs(A[i] - A[i+1]) - abs(A[i+1] - A[i+2]) + abs(A[i] - A[i+2])
print(*ans, sep='\n')
