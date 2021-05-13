import sys
def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    A = (N - M) * 100 + 1900 * M
    print(int(A * pow(2, M)))

    return 0

if __name__ == "__main__":
    solve()