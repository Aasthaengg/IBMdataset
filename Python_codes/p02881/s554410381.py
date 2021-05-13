# 約数列挙
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
d = make_divisors(n)
ans = 10**13
for i in d:
    j = n // i
    ans = min(ans, i+j-2)
print(ans)