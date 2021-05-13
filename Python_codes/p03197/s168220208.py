import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    N = int(input())
    first = False
    for _ in range(N):
        a = int(input())
        if a % 2 == 1: first = True
    if first: print("first")
    else: print("second")
    
            
    return 0

if __name__ == "__main__":
    solve()