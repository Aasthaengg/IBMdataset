def make_divisors(n):
    lower, upper = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower.append(i)
            if i != n // i:
                upper.append(n//i)
        i += 1
    return lower + upper[::-1]

cnt = 0
for i in range(1, int(input())+1, 2):
    if len(make_divisors(i)) == 8:
        cnt += 1
print(cnt)