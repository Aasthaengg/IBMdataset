#!/usr/bin/env python3
def main():
    N, K = map(int, input().split())
    P = [int(x) - 1 for x in input().split()]
    C = [int(x) for x in input().split()]

    ans = -10 ** 9
    for start in range(N):
        # ループを探索
        now = start
        cycle = []
        total = 0
        for _ in [0] * N:  # while Trueでもおｋ
            now = P[now]
            cycle.append(C[now])
            total += C[now]
            if now == start:
                break
        # 最大スコアを探索
        length = len(cycle)
        score = 0
        for move in range(length):
            score += cycle[move]
            # 移動回数 >= Kなら，ループ途中でも探索終了
            if move >= K:
                break
            # ループを周回するので，それを利用して探索を省略
            res = score
            if total > 0:
                laps = (K - (move + 1)) // length
                res += total * laps
            ans = max(ans, res)

    print(ans)


if __name__ == '__main__':
    main()
