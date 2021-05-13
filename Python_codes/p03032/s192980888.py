import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))

    ans = 0
    for n_pick in range(min(N, K) + 1):
        for left in range(n_pick + 1):
            right = n_pick - left
            tmp = []
            for i in range(left):
                tmp.append(V[i])
            for i in range(right):
                tmp.append(V[N - i - 1])
            tmp.sort()
            s = sum(tmp)
            n_return = min(K - n_pick, len(tmp))
            for i in range(n_return):
                if tmp[i] < 0:
                    s -= tmp[i]
                else:
                    break
            if s > ans:
                ans = s

    print(ans)


if __name__ == "__main__":
    main()
