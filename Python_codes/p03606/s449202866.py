import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    seat =  0
    for _ in range(N):
        l, r = map(int, input().split())
        seat += r - l + 1
    print(seat)
        

    return 0

if __name__ == "__main__":
    solve()