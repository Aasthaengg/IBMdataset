import sys

input = sys.stdin.readline


def main():
    a, b = input().split()
    if a == "H":
        print("H" if b == "H" else "D")
    else:
        print("D" if b == "H" else "H")


if __name__ == "__main__":
    main()
