N = int(input())
lim = int(N ** 0.5)
ans = 0
for i in range(1, lim + 1):
    m = N // i
    quotient = N // m
    while m != 0:
        remainder = N % m
        if N // m != quotient or remainder > i:
            break
        if quotient == remainder:
            ans += m
            break
        m -= 1
print(ans)
