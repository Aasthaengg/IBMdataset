def examC():
    N = I()
    A = LI()
    negative = []; positive = []
    ans = 0; ansC = []
    for i in A:
        if i<0:
            negative.append(i)
        else:
            positive.append(i)
    if negative==[]:
        positive.sort()
        if N>2:
            cur = positive[0] - positive[1]
            ansC.append([positive[0], positive[1]])
            ans = sum(positive) - 2 * positive[0]
            for i in range(2, N - 1):
                ansC.append([cur, positive[i]])
                cur -= positive[i]
            ansC.append([positive[N - 1], cur])
        else:
            ansC.append([positive[1],positive[0]])
            ans = positive[1]-positive[0]

    elif positive==[]:
        negative.sort(reverse=True)
        cur = negative[0] - negative[1]
        ansC.append([negative[0],negative[1]])
        ans = -sum(negative)+2*negative[0]
        for i in range(2,N):
            ansC.append([cur,negative[i]])
            cur -=negative[i]
    else:
        positive.sort()
        negative.sort(reverse=True)
        ans = sum(positive) - sum(negative)
        curN = negative[0]
        curP = positive[0]
        for i in range(len(positive)-1):
            ansC.append([curN,positive[i+1]])
            curN -=positive[i+1]
        for i in range(len(negative)-1):
            ansC.append([curP,negative[i+1]])
            curP -=negative[i+1]
        ansC.append([curP,curN])

    print(ans)
    for v in ansC:
        print(" ".join(map(str,v)))

from string import digits
import sys,copy,bisect,itertools,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examC()
