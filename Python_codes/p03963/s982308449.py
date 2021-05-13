import sys

def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    total = K
    for i in range(N-1): total *= (K - 1)
    print(total)
    return 0

if __name__ == "__main__":
    solve()