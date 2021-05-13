import sys
input = sys.stdin.readline


def main():
    a, b, c = map(int, input().split())

    y = (c - (a+b))**2 - 4*a*b
    if c-(a+b) > 0 and y > 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
