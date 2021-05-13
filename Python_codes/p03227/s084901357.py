from sys import stdin
import math
import re
import queue

input = stdin.readline

MOD = 1000000007
INF = 122337203685477580

def solve():
    N = (input().rstrip())

    if(len(N) == 3):
        N= ''.join(list(reversed(N)))
    
    print(N)
if __name__ == '__main__':
    solve()
