n, m, k = map(int, input().split())
l = lambda a, b: a * m + b * n - 2 * a * b
for n_ in range(n+1):
    for m_ in range(m+1):
        if l(n_, m_) == k:
            print("Yes")
            exit()
print("No")