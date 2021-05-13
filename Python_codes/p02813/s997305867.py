import sys
import itertools


def resolve(in_):
    N = int(next(in_))
    P = tuple(map(int, next(in_).split()))
    Q = tuple(map(int, next(in_).split()))

    p = 0
    q = 0
    for i, R in enumerate(itertools.permutations(range(1, N + 1), N), 1):
        if not p and P == R:
            p = i
            if q:
                break
        if not q and Q == R:
            q = i
            if p:
                break
    
    answer = abs(p - q)

    return answer


def main():
    answer = resolve(sys.stdin)
    print(answer)


if __name__ == '__main__':
    main()
