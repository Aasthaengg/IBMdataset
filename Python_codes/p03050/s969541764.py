def div(n):
    lower, upper = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower.append(i)
            if i != n // i:
                upper.append(n // i)
        i += 1
    return lower + upper[::-1]

n = int(input())
ans = 0
for i in div(n):
    if i == 1:
        continue
    elif n // (i - 1) == n % (i - 1):
        ans += i - 1
print(ans)
