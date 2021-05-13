import sys
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    MOD = 10 ** 9 + 7

    pos = []
    neg = []
    for a in A:
        if a >= 0:
            pos.append(a)
        else:
            neg.append(a)

    flag = False  # 積を正にできるか

    if N == K:
        ans = 1
        for a in A:
            ans *= a
            ans %= MOD
        print(ans % MOD)
        exit()

    if len(pos) > 0:
        flag = True
    else:
        if K % 2 == 0:
            flag = True

    ans = 1
    if not flag:
        # 積を正にできないとき
        # 絶対値の小さい方からK個とる
        h = [abs(x) for x in A]
        heapq.heapify(h)

        for i in range(K):
            ans *= heapq.heappop(h)
            ans %= MOD
        ans *= -1
    else:
        hpos = [-x for x in pos]
        heapq.heapify(hpos)
        hneg = neg[:]
        heapq.heapify(hneg)
        if K % 2 == 1:
            # Kが奇数の時
            # 一番大きい偶数を1つとる。
            ans *= -heapq.heappop(hpos)
            ans %= MOD

        # pos, neg sort -> 2個ずつペア -> 降順sort -> 上から K//2 個とる
        pairs = []
        while len(hpos) >= 2:
            x = -heapq.heappop(hpos)
            x *= -heapq.heappop(hpos)
            heapq.heappush(pairs, -x)
        while len(hneg) >= 2:
            x = heapq.heappop(hneg)
            x *= heapq.heappop(hneg)
            heapq.heappush(pairs, -x)
        if len(pairs):
            for i in range(K // 2):
                ans *= -heapq.heappop(pairs)
                ans %= MOD

    print(ans % MOD)


if __name__ == "__main__":
    main()
