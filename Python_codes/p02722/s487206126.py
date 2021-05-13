def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors


n = int(input())
a, b, ans = make_divisors(n), make_divisors(n-1), 0
for i in range(1, len(a)):
    tmp = n
    while tmp % a[i] == 0:
        tmp = tmp // a[i]
    if (tmp-1) % a[i] == 0:
        ans += 1
ans += len(b)
print(ans-1)