import sys


def solve(inp):
    r = int(inp.readline())

    return r * r


def main():
    result = solve(sys.stdin)
    if result:
        print(result)


if __name__ == '__main__':
    main()
