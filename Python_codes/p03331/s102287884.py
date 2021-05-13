from sys import stdin
import math
import re
import queue

input = stdin.readline

MOD = 1000000007
INF = 122337203685477580

def solve():
    N = int(input().rstrip())
    ANS = INF
    for i in range(1,N):
        ANS = min(ANS,sum(list(map(int, str(i)))) + sum(list(map(int, str(N - i)))))
    print(ANS)    

if __name__ == '__main__':
    solve()
