import sys
from itertools import islice, tee


def resolve(in_):
    A = int(next(in_))
    B = int(next(in_))
    C = int(next(in_))
    X = int(next(in_))

    ans = 0
    for a in range(A + 1):
        for b in range(B + 1):
            for c in range(C + 1):
                if a * 500 + b * 100 + c * 50 == X:
                    ans += 1

    return ans


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()
