import sys
from itertools import permutations

def solve():
    input = sys.stdin.readline
    a = int(input())
    b = int(input())
    h = int(input())
    print((a + b) * h // 2)
    return 0

if __name__ == "__main__":
    solve()