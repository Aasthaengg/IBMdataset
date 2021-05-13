import sys


def solve(inp):
    A = list(map(int, inp.readline().strip().split(' ')))

    return str((A[0] - 1) * (A[1] - 1))


def main():
    result = solve(sys.stdin)
    if result:
        print(result)


if __name__ == '__main__':
    main()
