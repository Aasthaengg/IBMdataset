import sys
def input(): return sys.stdin.readline().strip()


def main():
    N, M = map(int, input().split())
    cakes = [(0, 0, 0)]
    for _ in range(N):
        x, y, z = map(int, input().split())
        cakes.append((x, y, z))

    """
    これはdpするべきではなかった。O(NlogN)で解ける。
    単純にx+y+zやx-y-z等のそれぞれに対してcakesをソートして大きい値から取れば良い。
    """

    ans = 0
    for i in range(8):
        sorted_cakes = []
        for j in range(1, N + 1):
            S = 0
            for k in range(3): # iの立っているビットでx, y, zの符号を管理している！！
                if i & (1 << k):
                    S += cakes[j][k]
                else:
                    S -= cakes[j][k]
            sorted_cakes.append(S)
        sorted_cakes.sort()
        ans = max(ans, sum(sorted_cakes[N - M:]))
    print(ans)


if __name__ == "__main__":
    main()
