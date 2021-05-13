def calc(N, h, n):
    base = 4 * h * n - N * n - N * h
    if base <= 0:
        return False, -1
    ret = (N*h*n) / base
    return ret == int(ret) and 0 <= ret <= 3500, int(ret)

N = int(input())

def f(N):
    for h in range(1, 3501):
        for n in range(1, 3501):
            judge, ret = calc(N,h,n)
            if judge:
                return h, n, ret
    return -1, -1, -1

print(*f(N))
