import sys


def solve(inp):
    X = int(inp.readline().strip())

    if X < 1200:
        return "ABC"
    else:
        return "ARC"


def main():
    result = solve(sys.stdin)
    if result:
        print(result)


if __name__ == '__main__':
    main()
