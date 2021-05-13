import sys


def main():
    s = sys.stdin.readline().rstrip()

    black = 0
    ans = 0

    for i in s:
        if i == "B":
            black = black + 1
        else:
            ans = ans + black

    print(ans)


if __name__ == "__main__":
    main()