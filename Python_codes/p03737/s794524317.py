import sys

input = sys.stdin.readline


def main():
    s1, s2, s3 = input().split()
    ans = s1[0].upper() + s2[0].upper() + s3[0].upper()
    print(ans)


if __name__ == "__main__":
    main()
