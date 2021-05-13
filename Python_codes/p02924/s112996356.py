import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    print((N-1) * N // 2)

    return 0

if __name__ == "__main__":
    solve()