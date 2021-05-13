from sys import stdin
import math
import re
import queue

input = stdin.readline

MOD = 1000000007
INF = 122337203685477580

def solve():
    str = (input().rstrip())
    cnt = 0
    for s in str:
        if(s == '2'):
            cnt += 1
    
    print(cnt)
        
if __name__ == '__main__':
    solve()
