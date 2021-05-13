def dfs(i, p, seq):
    global N, M
    ret = 0
    if i == N:
        ret = check(seq)
    else:
        for x in range(p, M + 1):
            ret = max(ret, dfs(i + 1, x, tuple(list(seq) + [x])))
    return ret


def check(seq):
    cnt = 0
    for a, b, c, d in query:
        if seq[b - 1] - seq[a - 1] == c:
            cnt += d
    return cnt


N, M, Q = map(int, input().split())
query = [tuple(map(int, input().split())) for _ in range(Q)]

print(dfs(0, 1, tuple()))
