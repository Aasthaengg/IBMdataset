def div(n):
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
lis = list(set(div(n)))
ans = 0
for b in lis:
    c = b - 1
    if c != 0:
        
        if n//c == n%c:
            ans += c
print(ans)
