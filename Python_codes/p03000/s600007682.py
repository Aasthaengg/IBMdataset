import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    lsum = [0 for _ in range(N + 1)]
    for i in range(N):
        lsum[i + 1] = L[i] + lsum[i]

    for i in range(N + 1):
        if lsum[i] <= X:
            ans = i + 1
        else:
            break
    print(ans)


if __name__ == '__main__':
    solve()
