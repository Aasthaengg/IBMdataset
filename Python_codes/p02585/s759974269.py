#!/usr/bin/env python3
def main():
    N, K = map(int, input().split())
    P = [int(x) - 1 for x in input().split()]
    C = [int(x) for x in input().split()]

    ans = -10 ** 9
    for start in range(N):
        # ループを探す
        now = start
        loop = []
        total = 0
        while now != start or not loop:
            loop.append(C[now])
            now = P[now]
            total += C[now]
        # ループごとの最大スコアを探す
        length = len(loop)
        # sum_loop = sum(loop)
        # # ループ長よりも操作回数が多いか？，ループを周回すると得か？で場合分け
        # res = 0 if sum_loop <= 0 else sum_loop * (K // length)
        # limit = K if K <= length else K % length
        # for k in range(limit):
        #     res += loop[k]
        #     ans = max(ans, res)
        t = 0
        for i in range(length):
            t += loop[i]
            if i + 1 > K:
                break
            now = t
            if total > 0:
                e = (K - (i + 1)) // length
                now += total * e
            ans = max(ans, now)
    print(ans)


if __name__ == '__main__':
    main()
