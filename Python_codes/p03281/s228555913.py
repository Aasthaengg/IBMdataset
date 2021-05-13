def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

n = int(input())
# print(f"{n}")

ans = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        continue
    
    # d_count = sympy.divisor_count(i)
    a = make_divisors(i)
    # print(f"{i} {a}")
    d_count = len(a)
    # print(f"{i} {d_count}")
    if d_count == 8:
        ans += 1
print(ans)