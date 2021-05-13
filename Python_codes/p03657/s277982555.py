import sys


def solve(inp):
    A = list(map(int, inp.readline().strip().split(' ')))

    if A[0] % 3 == 0 or A[1] % 3 == 0 or sum(A) % 3 == 0:
        return "Possible"
    else:
        return "Impossible"


def main():
    result = solve(sys.stdin)
    if result:
        print(result)


if __name__ == '__main__':
    main()
