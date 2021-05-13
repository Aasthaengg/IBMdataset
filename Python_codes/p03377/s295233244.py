import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)


def main():
    A, B, X = [int(i) for i in input().strip().split()]
    for i in range(B+1):
        if A + i == X:
            return "YES"
    return "NO"


if __name__ == "__main__":
    print(main())
