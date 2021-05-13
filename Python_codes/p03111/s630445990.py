n, a, b, c = list(map(int, input().split(' ')))
ln = [None] * n
for i in range(n):
    ln[i] = (int(input()))


def dfs(i, ap, bp, cp):
    pattern = [ap, bp, cp]
    if i >= n and [] not in pattern:
        mp = 0
        for p in pattern:
            mp += max([0, len(p) - 1]) * 10
        mp += abs(a - sum(pattern[0]))
        mp += abs(b - sum(pattern[1]))
        mp += abs(c - sum(pattern[2]))
        return mp
    elif i >= n:
        return float('inf')
    else:
        return min([
            dfs(i + 1, ap + [ln[i]], bp, cp),
            dfs(i + 1, ap, bp + [ln[i]], cp),
            dfs(i + 1, ap, bp, cp + [ln[i]]),
            dfs(i + 1, ap, bp, cp)
        ])


result = dfs(0, [], [], [])
print(result)


