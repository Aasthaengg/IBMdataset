from collections import defaultdict

def diverta192_b():
    N = int(input())
    P = [tuple(map(int, input().split())) for _ in range(N)]
    if len(P) == 1:
        print(1)  # 座標が1つだけ与えられる場合は即終了
        return

    dcnt = defaultdict(int)  # import忘れずに
    for i in range(N):
        xi, yi = P[i]
        for j in range(i):
            xj, yj = P[j]
            dcnt[(xi-xj, yi-yj)] += 1
            dcnt[(xj-xi, yj-yi)] += 1  # 逆向きもカウントする(都合よいほうを使う)
    most = sorted(dcnt.values(), reverse=True)[0]  # 最も多いカウントを取り出す
    ans = N - most
    print(ans)

diverta192_b()