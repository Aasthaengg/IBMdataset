from numba import njit
@njit(cache=True)
def func(n, k, a):
    for i in range(k):
        b = []
        for i in range(n+1):
            b.append(0)
        for i in range(n):
            l = max(0, i - a[i])
            r = min(n, i + a[i] + 1)
            b[l] += 1
            b[r] -= 1
        for i in range(len(b)-1):
            b[i+1] += b[i]
        b = b[:n]
        if a == b:
            break
        else:
            a = b
    return b
if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = func(n, k, a)
    for i in range(n):
        print(b[i])
