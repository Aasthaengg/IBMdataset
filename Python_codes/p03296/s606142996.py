import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    N = int(input())
    A = [int(a) for a in input().split()]
    count = 0
    for i in range(1, N):
        if A[i] == A[i-1]:
            count += 1
            A[i] = -1
    print(count)


    return 0

if __name__ == "__main__":
    solve()