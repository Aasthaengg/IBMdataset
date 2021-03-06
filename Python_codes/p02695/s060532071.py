from itertools import combinations_with_replacement
n, m, q = map(int, input().split())
abcd = [list(map(int, input().split())) for i in range(q)]
ans = 0
for i in combinations_with_replacement(range(1, m + 1), n):
    cnt = 0
    for a, b, c, d in abcd:
        if i[b - 1] - i[a - 1] == c:
            cnt += d
    ans = max(ans, cnt)
print(ans)