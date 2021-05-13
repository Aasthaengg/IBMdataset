K, A, B = map(int, input().split())

if B - A <= 2:
    print(K + 1)
else:
    ans = 0
    # 初回のA枚→B枚まで A-1 回かかる
    rest = K - A + 1
    # このときにはA枚持っている
    ans += A
    # 残りをすべてA枚→B枚
    ans += rest // 2 * (B - A)
    if rest % 2 != 0:
        ans += 1
    print(ans)

