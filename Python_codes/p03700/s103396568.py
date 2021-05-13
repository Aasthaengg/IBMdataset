import sys

def solve():
    input = sys.stdin.readline
    N, A, B = map(int, input().split())
    H = [int(input()) for _ in range(N)]
    low = 0; high = 10 ** 20
    while high - low > 1:
        mid = (low + high) // 2
        explosion = B * mid
        direct = 0
        for h in H:
            if h - explosion > 0:
                direct += (h - explosion) // (A - B)
                if (h - explosion) % (A - B) > 0: direct += 1
        if direct <= mid: high = mid
        else: low = mid
    print(high)

    return 0

if __name__ == "__main__":
    solve()