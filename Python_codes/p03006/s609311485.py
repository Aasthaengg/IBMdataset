#!/usr/bin python3
# -*- coding: utf-8 -*-

from collections import Counter

def main():
    N = int(input())
    S = [tuple(map(int,input().split())) for _ in range(N)]

    if N == 1:
        print(1)
    else:
        cnt = []
        for i in range(N-1):
            xi, yi = S[i]
            for j in range(i+1,N):
                xj, yj = S[j]
                cnt.append((xi-xj, yi-yj))
                cnt.append((xj-xi, yj-yi))
        A = Counter(cnt)
        ll = max(A.values())
        print(N-ll)

if __name__ == '__main__':
    main()