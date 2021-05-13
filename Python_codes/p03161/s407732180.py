import sys

sys.setrecursionlimit(250000)
input = sys.stdin.readline
import queue


def main():
    n, k = map(int, input().split())
    h = list(map(int,input().split()))

    cost = [sys.maxsize]*n
    cost[0] = 0
    for i in range(0,n):
        for j in range(1, k + 1):
            if (i+ j>= n):
                break
            abs_ = abs(h[i] - h[i+j])
            if cost[i+j] >cost[i] + abs_ :
                cost[i+j] = cost[i] + abs_
    print(cost[n-1])
main()
