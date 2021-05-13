def examC():
    N = I()
    print(0)
    q = input()
    if q=="Vacant":
        exit()
    left = 0; right = N - 1
    for _ in range(20):
        cur = (left + right) // 2
        print(cur)
        next = input()
        if next=="Vacant":
            exit()

        if (cur % 2 == 1 and next == q) or (cur % 2 == 0 and next != q):
            right = cur
        else:
            left = cur + 1

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

if __name__ == '__main__':
    examC()
