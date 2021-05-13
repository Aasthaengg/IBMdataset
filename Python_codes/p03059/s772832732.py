import sys
from collections import defaultdict

def solve():
    input = sys.stdin.readline
    A, B, T = map(int, input().split())
    time = A
    count = 0
    while time < T + 0.5:
        count += B
        time += A
    print(count)

    return 0

if __name__ == "__main__":
    solve()