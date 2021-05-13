import bisect


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # 自分より数値が小さい数の個数
    # 1, 3, 2 --> [0, 2, 1]
    B = A.copy()
    B.sort()
    cnt = [0 for _ in range(N)]
    for i, a in enumerate(A):
        idx = bisect.bisect_left(B, a)
        cnt[i] = idx

    ans = 0
    MOD = 1000000007
    for c in cnt:
        ans += c * (K - 1) * K // 2
        ans %= MOD

    # 自分より後ろに存在する自分より小さい数の個数
    # 1, 3, 2 --> [0, 1, 0]
    B = A.copy()
    B = B[::-1]
    cnt = [0 for _ in range(N)]
    array = []
    for i, b in enumerate(B):
        idx = bisect.bisect_left(array, b)
        cnt[i] = idx
        bisect.insort_left(array, b)
    cnt = cnt[::-1]

    for c in cnt:
        ans += c * K
        ans %= MOD

    print(ans)
