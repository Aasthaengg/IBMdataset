import sys

def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    ans = (N // K) ** 3
    if K % 2 == 0:
        halfK = 0
        for i in range(1, N + 1):
            if i % K == K // 2: halfK += 1
        ans += (halfK) ** 3
    print(ans)

    return 0

if __name__ == "__main__":
    solve()