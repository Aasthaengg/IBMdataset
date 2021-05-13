N = int(input())
A = [int(input()) for _ in range(N)]
A2 = [index - a for index, a in enumerate(A)]


def solve():
    if A[0] != 0:
        return -1
    for i in range(N - 1):
        if A[i + 1] - A[i] > 1:
            return -1
    ans = 0
    for i in range(N - 1):
        if A2[i] != A2[i + 1]:
            ans += i - A2[i]
    else:
        i = N - 1
        ans += i - A2[i]
    return ans

print(solve())
