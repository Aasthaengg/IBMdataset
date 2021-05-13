import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def main():
    S =input()
    T =input()
    count =0
    for i in range(3):
        if S[i] ==T[i]:
            count +=1
    print(count)


if __name__ == "__main__":
    main()
