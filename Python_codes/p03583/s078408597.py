N = int(input())


def solve(h, n):
    if (4*h*n-N*n-N*h) == 0:
        return
    w = N*h*n // (4*h*n-N*n-N*h)
    if w < 1:
        return
    if w*(4*h*n-N*n-N*h) == N*h*n:
        print(h, n, w)
        exit()


if N < 2000:
    for h in range(1, 3501):
        for n in range(1, 3501):
            solve(h, n)
else:
    for h in reversed(range(1, 3501)):
        for n in reversed(range(1, 3501)):
            solve(h, n)
