import sys
import math
import heapq


def input():
    return sys.stdin.readline().rstrip()


def main():
    N=int(input())
    A=list(map(int,input().split()))


    print(sum(A)-N)

if __name__ == "__main__":
    main()

# \n
