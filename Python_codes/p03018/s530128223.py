import sys
# input = sys.stdin.buffer.readline
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getlist():
    return list(map(int, input().split()))
import math
import heapq
from collections import defaultdict, Counter, deque
MOD = 10**9 + 7
INF = 10**15


def main():
    ans = 0
    s = input().strip()
    # print(s)
    pre = ""
    state = ""
    cnta = 0
    for c in s:
        if c == "A":
            if state == "A":
                cnta += 1
            else:
                state = "A"
                cnta = 1
        if c == "B":
            if state == "A":
                state = "AB"
            else:
                state = ""
                cnta = 0
        if c == "C":
            if state == "AB":
                ans += cnta
                state = "A"
            else:
                state = ""
                cnta = 0

    print(ans)

if __name__ == '__main__':
    main()

"""
9999
3

2916
"""