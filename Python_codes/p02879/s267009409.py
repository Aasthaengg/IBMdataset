import sys

def solve():
    input = sys.stdin.readline
    A, B = map(int, input().split())
    if A < 10 and B < 10: print(A * B)
    else: print(-1)

    return 0

if __name__ == "__main__":
    solve()