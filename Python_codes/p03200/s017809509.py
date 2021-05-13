import sys

input = sys.stdin.readline


def main():
    S = input().rstrip()

    ans = 0
    n_black = 0
    for s in S:
        if s == "B":
            n_black += 1
        else:
            ans += n_black

    print(ans)


if __name__ == "__main__":
    main()
