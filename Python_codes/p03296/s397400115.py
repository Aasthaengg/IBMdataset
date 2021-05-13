from sys import stdin
import math
import re
import queue

input = stdin.readline

MOD = 1000000007
INF = 122337203685477580

def solve():
    N = int(input().rstrip())
    vec =list(map(int, input().split())) 
    prev = -1
    cnt = 1
    ANS = 0
    for x in vec:
        if(prev == x):
            cnt += 1
        else:
            prev = x
            ANS += cnt//2
            cnt = 1
    
    ANS += cnt//2
    print(ANS)

if __name__ == '__main__':
    solve()
