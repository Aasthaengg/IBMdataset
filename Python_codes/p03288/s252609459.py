import sys

input = sys.stdin.readline


def main():
    rate = int(input())
    if rate < 1200:
        print("ABC")
    elif rate < 2800:
        print("ARC")
    else:
        print("AGC")


if __name__ == "__main__":
    main()
