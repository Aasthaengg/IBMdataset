import sys

def solve():
    input = sys.stdin.readline
    N, T = map(int, input().split())
    A = [int(t) for t in input().split()]

    Ans = 0
    currentTime = A[0]
    for i in range(1, N):
        if A[i] - currentTime < T: Ans += A[i] - currentTime
        else: Ans += T
        currentTime = A[i]
    Ans += T
    print(Ans)
    return 0

if __name__ == "__main__":
    solve()