#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N = int(input())
    S = input()
    B = []
    W = []
    i = 0
    fin = None
    while i < N:
        if S[i] == '#':
            if i == N-1:
                B.append(1)
                fin = True
            else:
                tmp = 1
                while S[i+1] == '#':
                    tmp += 1
                    i += 1
                    if i == N-1:
                        fin = True
                        break
                B.append(tmp)
        else:
            if i == N-1:
                W.append(1)
                fin = False
            else:
                tmp = 1
                while S[i+1] == '.':
                    tmp += 1
                    i += 1
                    if i == N-1:
                        fin = False
                        break
                W.append(tmp)
        i += 1

    ans = sum(B)
    L = len(B)+len(W)
    B = B[::-1]
    W = W[::-1]
    now = ans
    if fin:
        for i in range(L):
            if i % 2 == 0:
                now -= B[i//2]
            else:
                now += W[i//2]
            ans = min(ans,now)
    else:
        for i in range(L):
            if i % 2 == 1:
                now -= B[i//2]
            else:
                now += W[i//2]
            ans = min(ans,now)
    print(ans)



    

if __name__ == "__main__":
    main()
