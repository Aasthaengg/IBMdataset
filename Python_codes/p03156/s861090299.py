from sys import stdin
import math
import re
import queue

input = stdin.readline

MOD = 1000000007
INF = 122337203685477580

def solve():
    N = int(input().rstrip())
    A,B = map(int, input().split())
    X =list(map(int, input().split())) 
    vec = [0]*3
    for x in X:
        if(x <= A):
            vec[0] += 1
        elif(x <= B):
            vec[1] += 1
        else:
            vec[2] += 1
    

    print(min(vec))
if __name__ == '__main__':
    solve()
