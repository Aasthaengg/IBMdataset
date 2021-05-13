import sys
from collections import deque
import itertools
from collections import deque
sys.setrecursionlimit(10 ** 9)

# map(int, sys.stdin.read().split())


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    print(N*(N-1)//2)




if __name__ == "__main__":
    main()
