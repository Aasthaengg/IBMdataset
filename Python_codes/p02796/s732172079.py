import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def keyence20_b():
    _ = int(readline())
    Robots = []
    for line in readlines():
        # (左端,右端) の形で格納
        x, l = map(int, line.strip().split())
        Robots.append((x-l, x+l))
    # 右端の昇順にソート
    Robots = sorted(Robots, key=lambda x: x[1])

    ans = 0
    x = -10**10  # 使用済み範囲
    for lf, rt in Robots:
        if x <= lf:
            ans += 1  # 他とぶつからないので採用(ゼロタッチは有効)
            x = rt
    print(ans)

keyence20_b()