n, m, d = [int(x) for x in input().split()]


def f():
    ans = 1
    if d != 0:
        ans = (m-1) * 2*(n-d)/(n*n)
    else:
        ans = (m-1)/n
    return ans


print(f())
