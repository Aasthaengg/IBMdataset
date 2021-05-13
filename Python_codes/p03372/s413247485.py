N, C = map(int, input().split())
XV = [[int(x) for x in input().split()] for _ in range(N)]

XV.sort()

def g():
    t_n = [(0, 0)] * (N + 1)
    ans = 0
    score = 0
    pos = 0
    for i, (x, v) in enumerate(XV, 1):
        score += v - (x - pos)
        pos = x
        ans = max(ans, score)
        t_n[i] = (pos, ans)
    
    t_r = [(0, 0)] * (N + 1)
    ans = 0
    score = 0
    pos = C
    for i, (x, v) in enumerate(reversed(XV), 1):
        score += v - (pos - x)
        pos = x
        ans = max(ans, score)
        t_r[i] = (pos, ans)
    
    ans = 0
    for i in range(1, N+1):
        ans = max(
                ans,
                t_n[i][1],
                t_r[i][1],
                t_n[i][1] -      t_n[i][0]  + t_r[N - i][1],
                t_r[i][1] - (C - t_r[i][0]) + t_n[N - i][1],
                )

    return ans

print(g())
