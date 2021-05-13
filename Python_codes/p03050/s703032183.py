n = int(input())


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


# 約数から1引いたものが候補
arr = make_divisors(n)
arr = [x - 1 for x in arr if x >= 2]

#　商と剰余が不一致ならbreakできる
ans = 0
for x in arr[::-1]:
    if n // x != n % x:
        break
    ans += x

print(ans)