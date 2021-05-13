n = int(input())

exponents = [0] * (n + 1)
for i in range(2, n + 1):
    x = i
    for j in range(2, i + 1):
        while x % j == 0:
            exponents[j] += 1
            x //= j

def f(x):
    return sum(exponent >= x - 1 for exponent in exponents)

ans = 0
ans += f(75)
ans += f(25) * (f(3) - 1)
ans += f(15) * (f(5) - 1)
ans += f(5) * (f(5) - 1) // 2 * (f(3) - 2)

print(ans)