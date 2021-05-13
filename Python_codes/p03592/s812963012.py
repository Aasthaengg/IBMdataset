import sys

def solve():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    possible = False
    for i in range(N + 1):
        for j in range(M + 1):
            black = (N - i) * j + i * (M - j)
            if black == K:
                print("Yes")
                possible = True
                break
        if possible: break
    else: print("No")

    return 0

if __name__ == "__main__":
    solve()