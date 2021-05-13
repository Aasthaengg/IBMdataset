import sys

input = sys.stdin.readline


def main():
    N = int(input())

    ans = "No"
    while N >= 0:
        if N % 4 == 0:
            ans = "Yes"
            break
        N -= 7

    print(ans)


if __name__ == "__main__":
    main()
