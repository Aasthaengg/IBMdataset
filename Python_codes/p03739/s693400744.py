n = int(input())
A = list(map(int, input().split()))


def solve(start):
    acc = [0] * n
    acc[0] = A[0]
    for i in range(1, n):
        acc[i] = acc[i - 1] + A[i]

    cur = start
    ans = 0
    x = 0
    for i in range(n):
        acc[i] += x
        if cur > 0:
            if acc[i] >= 0:
                ans += acc[i] + 1
                x -= acc[i] + 1
                acc[i] = -1
        else:
            if acc[i] <= 0:
                ans += abs(acc[i]) + 1
                x += abs(acc[i]) + 1
                acc[i] = 1
        cur = acc[i]
    return ans

ans = min(solve(1), solve(-1))
print(ans)