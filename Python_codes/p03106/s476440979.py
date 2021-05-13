def actual(a, b, k):
    M = max(a, b)

    common_divisors = []

    for i in range(1, M + 1):
        if (a % i == 0) and (b % i == 0):
            common_divisors.append(i)

    return common_divisors[-k]

a, b, k = map(int, input().split())
print(actual(a, b, k))