def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

n = int(input())
ans = 0

yakusu = make_divisors(n)

for i in yakusu:
    if i != 1 and (n//(i-1) == n%(i-1)):
        ans += i-1

print(ans)
