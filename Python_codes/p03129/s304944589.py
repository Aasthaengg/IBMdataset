from sys import stdin
import math
import re
import queue

input = stdin.readline

MOD = 1000000007
INF = 122337203685477580

def solve():
    N,K = map(int, input().split())
    if(K > N%2 + N/2):
        print("NO")
    else:
        print("YES")

    
if __name__ == '__main__':
    solve()
