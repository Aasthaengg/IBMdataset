import sys


def solve(inp):
    N = int(inp.readline().strip())

    return "ABC" + str(N)


def main():
    result = solve(sys.stdin)
    if result:
        print(result)


if __name__ == '__main__':
    main()
