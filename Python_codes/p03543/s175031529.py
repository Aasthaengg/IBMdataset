import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)


def main():
    N = input().strip()

    if N[0] == N[1] == N[2]:
        return "Yes"
    if N[1] == N[2] == N[3]:
        return "Yes"

    return "No"


if __name__ == "__main__":
    print(main())
