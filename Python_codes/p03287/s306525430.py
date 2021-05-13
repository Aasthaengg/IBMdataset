def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    t = A[0] % M
    d = {}
    d[t] = 1
    for i in A[1:]:
        t += i
        t %= M
        if t in d:
            d[t] += 1
        else:
            d[t] = 1
    r = 0
    for i in d:
        r += (d[i] * (d[i] - 1)) // 2
    if 0 in d:
        r += d[0]
    return r
print(main())
