n, m = map(int, input().split())


def make_divisors(num):
    divisors = []
    for i in range(1, m+1):
        if i * i > m:
            break
        if m % i == 0:
            divisors.append(i)
            divisors.append(m // i)
    return divisors

div = make_divisors(num=m)
div.sort()
ans = 1
for x in div:
    if x*n <= m:
        ans = x
print(ans)
