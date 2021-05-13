# https://atcoder.jp/contests/abc054/submissions/4360181

def main():
    from collections import defaultdict

    INF = 40 * 100 + 1

    N, Ma, Mb = map(int, input().split())

    memo = defaultdict(lambda: INF)

    for _ in range(N):
        ai, bi, ci = map(int, input().split())
        x = Ma * bi - Mb * ai  # Σai:Σbi=Ma:Mb<->Ma*Σbi-Mb*Σai=0

        for key, value in tuple(memo.items()):
            memo[key + x] = min(
                memo[key + x],
                value + ci
            )  # 既存の組み合わせに混合
        memo[x] = min(memo[x], ci)  # 新規のみ

    print(memo[0] if 0 in memo else -1)


if __name__ == '__main__':
    main()
