import sys

input = sys.stdin.readline


def main():
    b = input().rstrip()

    if b == "A":
        ans = "T"
    elif b == "T":
        ans = "A"
    elif b == "G":
        ans = "C"
    else:
        ans = "G"

    print(ans)


if __name__ == "__main__":
    main()
