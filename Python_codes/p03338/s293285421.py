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
S = input()
X = [0]*26
Y = [0]*26

for i in range(N):
    k = ord(S[i])-ord('a')
    Y[k] += 1

ans = 0
for i in range(N):
    k = ord(S[i])-ord('a')
    X[k] += 1
    Y[k] -= 1
    tmp = 0
    for j in range(26):
        if X[j]>0 and Y[j]>0:
            tmp += 1
    ans = max(ans,tmp)
print(ans)