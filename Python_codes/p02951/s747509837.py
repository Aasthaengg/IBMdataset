import sys

def solve():
    input = sys.stdin.readline
    A, B, C = map(int, input().split())
    print(max(0, C - A + B))

    return 0

if __name__ == "__main__":
    solve()