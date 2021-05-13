import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    AB = [[] for _ in range(N)]
    for i in range(N):
        AB[i] = list(map(int, input().split()))

    AB.sort(key=lambda x: x[1])
    asum = [0 for _ in range(N + 1)]
    for i in range(N):
        asum[i + 1] = asum[i] + AB[i][0]

    ans = 'Yes'
    for i in range(N):
        if asum[i + 1] > AB[i][1]:
            ans = 'No'
            break

    print(ans)


if __name__ == '__main__':
    solve()
