import sys

def f(fl, i, j):
    return sum(1 for v in fl if v[0] == i and v[1] == j)


def first_last(N):
    for n in range(1, N + 1):
        last = n % 10

        while n >= 10:
            n, _ = divmod(n, 10)
        first = n
        yield first, last


def resolve(in_):
    N = int(next(in_).strip())
    fl = tuple(first_last(N))
    
    ans = sum(f(fl, i, j) * f(fl, j, i) for i in range(10) for j in range(10))
    return ans


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()
