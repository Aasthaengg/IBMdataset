import sys

def solve():
    input = sys.stdin.readline
    A, B, C = map(int, input().split())
    print(min(C, B//A))

    return 0

if __name__ == "__main__":
    solve()