import sys
input = sys.stdin.readline


def main():
    a, b, t = [int(i) for i in input().strip().split()]
    print(b * (t // a))
    return


if __name__ == "__main__":
    main()