n = int(input())
F = [tuple(int(x) for x in input().split()) for _ in range(n)]
P = [tuple(int(x) for x in input().split()) for _ in range(n)]
ans = -10**18
for bit in range(1, 1<<10):
    A = [0] * n  # 被り数
    for i in range(10):
        if bit & (1<<i):  # 開店
            for j in range(n):
                if F[j][i] == 1:
                    A[j] += 1
    profit = 0
    for j in range(n):
        profit += P[j][A[j]]
    ans = max(ans, profit)
print(ans)
