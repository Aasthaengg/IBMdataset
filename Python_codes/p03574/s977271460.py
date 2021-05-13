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

H,W = mint()
S = [input() for _ in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j]=='#':
            print('#',end='')
        else:
            tmp = 0
            for a in [-1,0,1]:
                for b in [-1,0,1]:
                    if (a,b)!=(0,0) and 0<=i+a<H and 0<=j+b<W and S[i+a][j+b]=='#':
                        tmp += 1
            print(tmp,end='')
    print('')