import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)


def main():
    n = int(input().strip())
    s = set()
    for i in range(n):
        s.add(input().strip())
    print(len(s))
    return


if __name__ == "__main__":
    main()
