from sys import stdin
import math
import re
import queue

input = stdin.readline

MOD = 1000000007
INF = 122337203685477580

def solve():
    vec = [0]*4
    for x in range(3):
        A,B = map(int, input().split())
        A -= 1
        B -=1
        vec[A] += 1
        vec[B] += 1
    
    if(vec[0] == 1 and vec[1] == 2 and vec[2] == 2 and vec[3] == 1):
        print("YES")
    else:
        print("NO")



if __name__ == '__main__':
    solve()
