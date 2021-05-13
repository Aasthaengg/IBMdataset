import sys
from heapq import heapify, heappop, heappush
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

k = int(input())
a = [int(i) for i in range(1, 10)]

heapify(a)
while len(a):
    tmp = heappop(a)
    keta = len(str(tmp))
    one = tmp % 10
    k -= 1
    for i in range(0, 10):
        if abs(one - i) <= 1:
            heappush(a, tmp * 10 + i)
    if k == 0:
        print(tmp)
        exit()
