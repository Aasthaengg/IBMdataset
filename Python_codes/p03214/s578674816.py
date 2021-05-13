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

    avg = sum(vec)/len(vec)
    for x in range(len(vec)):
        vec[x] = (vec[x] - avg)**2
    
    # print(vec)
    MIN = INF
    ANS = 0
    for i,x in enumerate(vec):
        if(MIN > x):
            MIN = x
            ANS = i

    print(ANS)


    print("")
if __name__ == '__main__':
    solve()
