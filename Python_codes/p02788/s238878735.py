import bisect


def main():
    N, D, A = list(map(int, input().split()))
    monsters = [list(map(int, input().split())) for _ in range(N)]
    monsters.sort()
    X = [m[0] for m in monsters]
    # 端から貪欲に攻撃していく
    ans = 0
    damages = [0] * (N + 1)
    for n, monster in enumerate(monsters):
        x, h = monster
        h = max(0, h - damages[n])
        to_n = bisect.bisect_right(X, x + 2 * D)
        cnt = (h + A - 1) // A  # ceil(h / A)
        ans += cnt
        damages[n] += A * cnt
        damages[to_n] -= A * cnt
        damages[n + 1] += damages[n]
    print(ans)


if __name__ == '__main__':
    main()