from sys import stdin
import math
import re
import queue

input = stdin.readline

MOD = 1000000007
INF = 122337203685477580

def solve():
    A,B,C,K = map(int, input().split())

    x = ((-1)**(K%2))*(A- B)

    if(x>1e18):
        print("Unfair")

    print(x)
if __name__ == '__main__':
    solve()
