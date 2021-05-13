from sys import stdin
import math
import re
import queue

input = stdin.readline

MOD = 1000000007
INF = 122337203685477580

def solve():
    S = (input().rstrip())
    ref = "CODEFESTIVAL2016"

    cnt = 0
    for x in range(len(ref)):
        if(S[x] != ref[x]):
            cnt += 1
    
    print(cnt)
   


if __name__ == '__main__':
    solve()
