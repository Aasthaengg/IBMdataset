#!/usr/bin/env python3

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    f = list(map(int, input().split()))
    a = sorted(a)
    f = sorted(f)
    f = f[::-1]
    mi = -1  # Impossible
    ma = 10 ** 12  # Possible
    for i in range(100):
        md = mi + (ma - mi) // 2
        if can_achieve(md, a, f, k, n):
            ma = md
        else:
            mi = md
        if ma - mi <= 1:
            break
    print(ma)

def can_achieve(score, a, f, k, n):
    sumb = 0
    for i in range(n):
        b = a[i] - score // f[i]
        b = max(b, 0)
        sumb += b
    return k >= sumb

if __name__ == "__main__":
    main()
