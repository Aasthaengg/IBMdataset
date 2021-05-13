#!/usr/bin/env python3
import sys
from collections import defaultdict
# input = sys.stdin.readline
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LI(): return list(map(int,input().split()))


def main():
    N = INT()
    AB = [LI() for _ in range(N)]
    AB.sort(key=lambda x: -(x[0]+x[1]))

    answer = 0
    for i in range(N):
        if i%2 == 0:
            answer += AB[i][0]
        else:
            answer -= AB[i][1]
    
    print(answer)

    return


if __name__ == '__main__':
    main()
