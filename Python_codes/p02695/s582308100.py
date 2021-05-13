from itertools import combinations_with_replacement
N, M, Q = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(Q)]

ans = 0
for pattern in combinations_with_replacement(range(1, M + 1), N):
    tmp_ans = 0
    pattern = list(pattern)
    for a, b, c, d in X:
        if pattern[b - 1] - pattern[a - 1] == c:
            tmp_ans += d
    ans = max(ans, tmp_ans)

print(ans)