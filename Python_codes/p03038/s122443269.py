import sys


def read():
    return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, read().split())
    a = sorted(int(i) for i in read().split())
    bc = [(0, 0) for _ in range(m)]
    for i in range(m):
        b, c = map(int, read().split())
        bc[i] = (c, b)
    bc.sort(reverse=True)
    k = 0
    d = []
    for c, b in bc:
        if k + b > n:
            d += [c] * (n - k)
            break
        d += [c] * b
        k += b
    for i in range(len(d)):
        if a[i] < d[i]:
            a[i] = d[i]
        else:
            break
    print(sum(a))


if __name__ == '__main__':
    main()
