import sys

input = sys.stdin.readline


def main():
    c1 = input().rstrip()
    c2 = input().rstrip()
    c3 = input().rstrip()

    ans = c1[0] + c2[1] + c3[2]

    print(ans)


if __name__ == "__main__":
    main()
