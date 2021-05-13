import sys
input = sys.stdin.readline


def main():
    S = input().rstrip()
    count = 0
    ans = 0
    for s in S:
        if s == "S":
            count += 1
        if s == "T":
            count -= 1
        if count < 0:
            ans += 1
            count = 0

    print(ans+count)


if __name__ == "__main__":
    main()
