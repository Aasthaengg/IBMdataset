from sys import stdin
import math
import re
import queue

input = stdin.readline

MOD = 1000000007
INF = 122337203685477580

def solve():
    N = int(input().rstrip())
    S1 = (input().rstrip())
    S2 = (input().rstrip())
    S3 = (input().rstrip())
    cnt = 0
    for x in range(N):
        ic = 0
        if(S1[x] == S2[x]):
            ic += 1
        if(S3[x] == S2[x]):
            ic += 1
        if(S1[x] == S3[x]):
            ic += 1    

        if(ic == 1):
            cnt += 1
        elif(ic < 1):
            cnt += 2
        else:
            cnt += 0
    
    print(cnt)

if __name__ == '__main__':
    solve()
