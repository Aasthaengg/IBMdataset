import sys

input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    _V = V[::-1]

    ans = 0
    for k in range(K + 1):
        n_pop = min(k, N)
        n_push = K - n_pop
        for i in range(n_pop + 1):
            l, r = i, n_pop - i
            L = V[:l] + _V[:r]
            L.sort()
            for j in range(min(n_pop, n_push)):
                if L[j] < 0:
                    L[j] = 0
                else:
                    break
            v = sum(L)
            if v > ans:
                ans = v

    print(ans)


if __name__ == "__main__":
    main()
