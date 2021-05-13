def main():
    from itertools import combinations

    N = int(input())
    F = []
    for _ in range(N):
        t = 0
        for j, b in enumerate(map(int, input().split())):
            if b:
                t |= (1 << j)
        F.append(t)
    # F[i]:=店舗iの営業時間情報
    P = [list(map(int, input().split())) for _ in range(N)]
    # P[i]:=店舗iと営業時間が重なる個数に対する利益

    ans = -10 ** 9 - 1
    for open_ in range(1, 10 + 1):
        for comb in combinations(range(10), r=open_):
            t = 0
            for j in comb:
                t |= (1 << j)

            p = 0
            for i, f in enumerate(F):
                x = bin(t & f).count('1')
                p += P[i][x]

            ans = max(ans, p)

    print(ans)


if __name__ == '__main__':
    main()
