import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)


def main():
    R = int(input())
    if R < 1200:
        print("ABC")
    elif 1200 <= R and R < 2800:
        print("ARC")
    else:
        print("AGC")


if __name__ == "__main__":
    main()
