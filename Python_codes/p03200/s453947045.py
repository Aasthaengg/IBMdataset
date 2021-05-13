import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    S = input().strip()

    ans = 0
    b = 0
    for s in S:
        if s == "B":
            b += 1
        else:
            ans += b

    print(ans)


if __name__ == '__main__':
    main()
