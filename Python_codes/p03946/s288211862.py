def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))

    mi = 10**10
    diff = 0
    r = 0
    for a in A:
        if a < mi:
            mi = a
        elif a - mi == diff:
            r += 1
        elif a - mi > diff:
            r = 1
            diff = a - mi
    return r

print(main())
