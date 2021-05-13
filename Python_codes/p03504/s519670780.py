N, C = [int(_) for _ in input().split()]

MT = (10 ** 5 + 10)

memo = [[0] * C for _ in range(MT)]

stc = sorted([[int(_) for _ in input().split()] for _ in range(N)])
for s, t, c in stc:
    if memo[s][c - 1] < 0:
        memo[s][c - 1] = 0
    else:
        memo[s - 1][c - 1] += 1
    memo[t][c - 1] -= 1
ans = 0
cnt = 0
for i in range(MT):
    cnt += sum(memo[i])
    ans = max(ans,cnt)
print(ans)
