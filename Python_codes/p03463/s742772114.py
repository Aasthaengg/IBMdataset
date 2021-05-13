import sys

def solve():
    input = sys.stdin.readline
    N, A ,B = map(int, input().split())
    if abs(A - B) % 2 == 1: print("Borys")
    else: print("Alice")

    return 0

if __name__ == "__main__":
    solve()