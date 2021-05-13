N = int(input())
A = [int(_) for _ in input().split()]


def judge(x, y):
    return x & y == 0


l = 0
r = -1
x = 0
ans = 0
while l < N:

    while r + 1 < N and judge(x, A[r + 1]):
        x ^= A[r + 1]
        r += 1

    ans += r - l + 1
    x ^= A[l]
    l += 1
print(ans)
