from sys import stdin
import math
import re
import queue

input = stdin.readline

MOD = 1000000007
INF = 122337203685477580

def solve():
    str = (input().rstrip())
    FC = INF
    LF = 0
    for x in range(len(str)):
        if(str[x] == 'C'):
            FC = min(FC,x+1)
        if(str[x] =='F'):
            LF = max(LF,x+1)
    
    if(FC*LF > 0 and LF > FC):
        print("Yes")
    else:
        print("No")


    print("")
if __name__ == '__main__':
    solve()
