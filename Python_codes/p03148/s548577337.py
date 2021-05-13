def solve(n, k, t, d):
    que = []
    used = set()
    base_score = 0
    for ti, di in sorted(zip(t, d), key=lambda _:-_[1])[:k]:
        if ti in used:
            que.append(di)
        else:
            used.add(ti)
        base_score += di
    num = len(used)
    best = base_score + num**2

    M = {}
    for ti, di in zip(t, d):
        if not ti in used:
            if not ti in M:
                M[ti] = 0
            M[ti] = max(M[ti], di)

    que = sorted(que)
    for i, p in enumerate(sorted(M.values())[::-1][:len(que)]):
        base_score += p - que[i]
        num += 1
        best = max(best, base_score + num**2)
    return best

n, k = map(int, input().split())
t = [0] * n
d = [0] * n
for i in range(n):
    t[i], d[i] = map(int, input().split())
print(solve(n, k, t, d))