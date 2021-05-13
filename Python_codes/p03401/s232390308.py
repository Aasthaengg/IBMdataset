N = int(input())
A = [0] + list(map(int, input().split())) + [0]

C = [0] * (N + 1)
S = 0
for i in range(N + 1):
    l = abs(A[i + 1] - A[i])
    C[i] = l
    S += l

ans = []
for i in range(1, N + 1):
    rst = S
    rst -= C[i] + C[i - 1]
    rst += abs(A[i + 1] - A[i - 1])
    ans.append(rst)

print(*ans, sep='\n')
