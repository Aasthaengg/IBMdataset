import sys
input = sys.stdin.readline

N, A, B = map(int, input().split())
H = tuple(int(input()) for _ in range(N))


def ceil(a, b):
    return (a + b - 1) // b


def f(x):
    lst = (max(0, h - x * B) for h in H)
    S = sum(ceil(i, A - B) for i in lst)
    return S <= x


l, r = 0, 10 ** 9
while r - l > 1:
    m = (r + l) // 2
    if f(m):
        r = m
    else:
        l = m
print(r)
