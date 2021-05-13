from sys import stdin
import math
import re
import queue

input = stdin.readline

MOD = 1000000007
INF = 122337203685477580

def solve():
    N,X,Y = map(int, input().split())
    print(min(X,Y),max(0,X + Y - N))
    
if __name__ == '__main__':
    solve()
