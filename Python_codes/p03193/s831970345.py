from sys import stdin
import math
import re
import queue

input = stdin.readline

MOD = 1000000007
INF = 122337203685477580

def solve():
    N,H,W = map(int, input().split())
    cnt = 0
    for x in range(N):
        h,w = map(int, input().split())
        if(h >= H and w >= W):
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    solve()
