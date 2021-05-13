from sys import stdin
import math
import re
import queue

input = stdin.readline

MOD = 1000000007
INF = 122337203685477580

def solve():
    vec =list(map(int, input().split())) 
    vec.sort()
    if(vec[0] == 1 and vec[1] == 4 and vec[2] == 7 and vec[3] == 9):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()
