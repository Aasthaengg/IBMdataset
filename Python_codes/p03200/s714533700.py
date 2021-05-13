import sys

input = sys.stdin.readline


def main():
    S = input().rstrip()

    ans = 0
    n_white = 0
    for s in S[::-1]:
        if s == "W":
            n_white += 1
        else:
            ans += n_white

    print(ans)


if __name__ == "__main__":
    main()
