import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def combdp():
    n = 50
    comb = [[0] * (n + 1) for _ in range(n + 1)]
    comb[0][0] = 1

    for i in range(1, n + 1):
        comb[i][0] = 1
        for j in range(1, i + 1):
            comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j])

    return comb


def main():
    n, a, b = map(int, readline().split())
    v = list(map(int, readline().split()))
    v.sort()
    v.reverse()

    comb = combdp()
    val = [0] * (n + 1)
    cnt = [0] * (n + 1)

    for i in range(a, b + 1):
        val[i] = sum(v[:i])
        mn = min(v[:i])
        c1 = v.count(mn)
        ct = 0
        for j in range(n):
            if v[j] > mn:
                ct += 1
        c2 = i - ct
        cnt[i] = comb[c1][c2]

    ans_val = 0
    ans_cnt = 0

    for i in range(a, b + 1):
        for j in range(a, b + 1):
            x = val[i] * j
            y = val[j] * i
            if x >= y:
                pass
            else:
                break
        else:
            ans_val = val[i] / i
            ans_cnt += cnt[i]

    print(ans_val)
    print(ans_cnt)


if __name__ == '__main__':
    main()
