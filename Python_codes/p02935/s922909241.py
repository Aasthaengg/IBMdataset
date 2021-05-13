import sys

# import bisect
# import numpy as np
from collections import deque
# map(int, sys.stdin.read().split())



def input():
    return sys.stdin.readline().rstrip()


def main():
    N =int(input())
    V =list(map(int,input().split()))
    V.sort()
    sum =V[0]
    for i in range(1,N):
        sum = sum/2 +V[i]/2
    print(sum)



if __name__ == "__main__":
    main()
