import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


def main():
    S =input()
    for i in range(3):
        if S[i] ==S[i+1]:
            print("Bad")
            exit()

    print("Good")


if __name__ == "__main__":
    main()
