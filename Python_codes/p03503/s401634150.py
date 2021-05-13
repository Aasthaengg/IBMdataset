from itertools import product


def main():
    N = int(input())
    F = [list(map(int, input().split(' '))) for _ in range(N)]
    P = [list(map(int, input().split(' '))) for _ in range(N)]
    ans = - 10**10
    for pattern in product([0, 1], repeat=10):
        if sum(pattern) == 0:
            continue
        profit = 0
        for n in range(N):
            c = sum([1 if p == f == 1 else 0 for p, f in zip(pattern, F[n])])
            profit += P[n][c]
        ans = max([ans, profit])
    print(ans)


if __name__ == '__main__':
    main()
