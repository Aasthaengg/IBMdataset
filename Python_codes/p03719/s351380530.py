import sys


def solve(inp):
    A = list(map(int, inp.readline().strip().split(' ')))

    if A[0] <= A[2] <= A[1]:
        return "Yes"
    else:
        return "No"


def main():
    result = solve(sys.stdin)
    if result:
        print(result)


if __name__ == '__main__':
    main()
