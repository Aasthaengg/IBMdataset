def m_pow(x, n) -> int:
    """
    O(log n)
    """
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x
        x *= x
        n //= 2

    return (K * x)


ans = 1
x = int(input())
for i in range(2, 1001):
    for j in range(2, 1001):
        n = m_pow(i, j)
        if n <= x:
            ans = max(n, ans)
        else:
            break

print(ans)
