n, m, q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(q)]
ans = 0
seq = [0] * 10

def dfs(depth, tail):
    global ans, seq
    if depth == n:
        s = 0
        for a, b, c, d in abcd:
            a -= 1
            b -= 1
            if seq[b] - seq[a] == c:
                s += d
        ans = max(ans, s)
        return

    for i in range(tail, m + 1):
        seq[depth] = i
        dfs(depth + 1, i)

dfs(0, 1)
print(ans)