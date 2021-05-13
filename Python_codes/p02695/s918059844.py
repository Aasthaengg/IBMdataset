import sys
import itertools


def resolve(in_):
    n, m, q = map(int, next(in_).split())
    abcd = tuple(tuple(map(int, row.split())) for row in in_)
    # print(abcd)

    ans = 0
    for seq_a in itertools.combinations_with_replacement(range(1, m + 1), n):
        # print(seq_a)
        point = 0
        for a, b, c, d in abcd:
            if seq_a[b - 1] - seq_a[a - 1] == c:
                point += d
        ans = max(ans, point)

    return ans


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()