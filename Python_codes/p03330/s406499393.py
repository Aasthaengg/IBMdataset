
from itertools import permutations


def submit():
    n, c = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(c)]    
    color = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(n)]
    color_cnt = {i: {cl: 0 for cl in range(c)} for i in range(3)}

    for i in range(n):
        for j in range(n):
            color_cnt[(i + j) % 3][color[i][j]] += 1

    ans = float('inf')
    for c0, c1, c2 in permutations(range(c), 3):
        t = 0
        for cl in range(c):
            t += color_cnt[0][cl] * d[cl][c0]
            t += color_cnt[1][cl] * d[cl][c1]
            t += color_cnt[2][cl] * d[cl][c2]
        if t < ans:
            ans = t
    print(ans)


submit()