def divisor(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)

        i += 1

    return lower_divisors + upper_divisors[::-1]

n = int(input())
d = divisor(n)
if len(d) == 2:
    print(d[1] - 1)
elif len(d) % 2 == 0:
    k = len(d)//2
    u = d[k-1]
    v = d[k]
    print((u-1) + (v-1))
else:
    k = len(d)//2
    v = d[k]
    print((v-1)*2)
