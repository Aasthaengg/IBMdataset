import sys


def solve(inp):
    (X, A, B) = map(int, inp.readline().strip().split(' '))

    if abs(X - A) < abs(X - B):
        return "A"
    else:
        return "B"


def main():
    result = solve(sys.stdin)
    if result:
        print(result)


if __name__ == '__main__':
    main()
