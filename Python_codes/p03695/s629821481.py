import sys
from collections import deque
from bisect import bisect_left, bisect_right, insort_left, insort_right #func(リスト,値)
from heapq import heapify, heappop, heappush

sys.setrecursionlimit(10**6)
INF = 10**20

def mint():
    return map(int,input().split())
def lint():
    return map(int,input().split())
def judge(x, l=['Yes', 'No']):
    print(l[0] if x else l[1])

N = int(input())
A = lint()
S = set()
pro = 0
for a in A:
    if a//400<8:
        S.add(a//400)
    else:
        pro += 1
print(max(1,len(S)),len(S)+pro)