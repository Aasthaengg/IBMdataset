import sys

def solve():
    N, K = [int(i) for i in input().split()]
    H = []
    for _ in range(N):
        H.append(int(input()))
    H.sort()
    ans = sys.maxsize
    for i in range(N - K + 1):
        ans = min(ans, H[i + K - 1] - H[i])
    print(ans)

if __name__ == "__main__":
    solve()