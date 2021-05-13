import sys

def solve():
    input = sys.stdin.readline
    N, H, W = map(int, input().split())
    count = 0
    for i in range(N):
        A, B = map(int, input().split())
        if A >= H and B >= W: count += 1
    print(count)
    return 0

if __name__ == "__main__":
    solve()