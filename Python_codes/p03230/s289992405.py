def examA():
    S = SI()
    if len(S)==3:
        ans = S[::-1]
    else:
        ans = S
    print(ans)
    return

def examB():
    A, B, K = LI()
    for i in range(K):
        if i%2==0:
            B +=A//2
            A //=2
        else:
            A +=B//2
            B //=2
    print(A,B)
    return

def examC():
    N = I()
    A = [I() for _ in range(N)]
    A.sort()
    A1 = A[:N//2]; A2 = A[N//2:]
    ans = 0; cur = 0
    for i in range(len(A2)):
        if i<len(A1):
            cur +=(A2[i]-A1[i])
        if i-1>=0:
            cur +=(A2[i]-A1[i-1])
    if N%2==1:
        cur += (A2[-1] - A2[1])
    ans = max(ans,cur)
#    print(A1,A2)
#    print(ans)
    if N%2==1:
        A1 = A[:1+(N//2)]; A2 = A[1+(N//2):]
        cur = 0
        for i in range(len(A1)):
            if i < len(A2):
                cur += (A2[i] - A1[i])
            if i - 1 >= 0:
                cur += (A2[i-1] - A1[i])
        cur +=(A1[-2]-A1[0])
        ans = max(ans, cur)
#    print(A1,A2)
    print(ans)
    return

def examD():
    N = I()
    ansCandi = []
    for i in range(1, 1000):
        a = (i + 1) * i / 2
        ansCandi.append(a)
    if N not in ansCandi:
        print("No")
    else:
        a = ansCandi.index(N) + 1
        A = [[0] * (a + 1) for _ in range(a + 1)]
    #    print(a)
        k = int(1)
        for i in range(a + 1):
            for j in range(i + 1, a + 1):
                A[i][j] = k
                A[j][i] = k
                k += 1
#        print(A)
        print("Yes")
        print(a + 1)
        for v in A:
            v.remove(0)
            v.insert(0, a)
        for v in A:
            print(*v)
    return

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
    examD()
