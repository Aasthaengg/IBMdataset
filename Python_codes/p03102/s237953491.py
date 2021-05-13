import sys
import bisect
import heapq
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def sump(x, y, z, t):
    ans = z
    for i in range(t):
        ans += x[i] * y[i]

    return ans

def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    count =0
    for j in range(N):
        A = list(map(int,input().split()))
        if sump(A,B,C,M) >0:
            count +=1

    print(count)

if __name__ == "__main__":
    main()
