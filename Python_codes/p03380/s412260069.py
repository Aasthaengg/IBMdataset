def check(n, m):
    l = n // 2
    r = l + (n % 2 == 1)

    return min(abs(l - m), abs(r - m))


N = int(input())
A = list(map(int, input().split()))

A.sort()
n = A[-1]
pd = float('inf')
for i in range(N - 1):
    a = A[i]
    d = check(n, a)
    if d < pd:
        b = a
        pd = d
print(n, b)
