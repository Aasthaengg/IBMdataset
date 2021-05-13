import sys
import itertools

input = sys.stdin.readline


def main():
    N = int(input())
    balls = [tuple(map(int, input().split())) for _ in range(N)]
    comb = list(itertools.combinations(balls, 2))
    ans = 0
    for c in comb:
        a, b = c
        p = b[0] - a[0]
        q = b[1] - a[1]
        ans_i = 0
        for d in balls:
            e = (d[0] + p, d[1] + q)
            if e in balls:
                ans_i += 1
        ans = max(ans, ans_i)
    print(N - ans)


if __name__ == '__main__':
    main()
