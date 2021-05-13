def binary_search(c1, c2):
    m = (c1 + c2 + 1) // 2
    if abs(c1 - c2) <= 1:
        return m
    else:
        s = list(h)
        c = 0
        for j in s:
            j -= b * m
            if j > 0:
                c += (a + j - b - 1) // (a - b)
            if c > m:
                break
        if c > m:
            c1 = m
        else:
            c2 = m
        return binary_search(c1, c2)

n, a, b = map(int, input().split())
h = [int(input()) for _ in range(n)]
h.sort()
print(binary_search(0, h[n - 1] + 1))