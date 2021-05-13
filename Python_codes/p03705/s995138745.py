import sys

def solve():
    input = sys.stdin.readline
    N, A, B = map(int, input().split())
    if A > B: print(0)
    elif N == 1:
        if B != A: print(0)
        else: print(1)
    else:
        rem = N - 2
        minS = A + B + rem * A
        maxS = A + B + rem * B
        print(maxS - minS + 1)

    return 0

if __name__ == "__main__":
    solve()