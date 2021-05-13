n = int(input())

div = []
for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        div.append(i)
        if i ** 2 != n:
            div.append(n // i)

cnt = 0
for i in range(1, int((n-1)**0.5)+1):
    if (n - 1) % i == 0:
        if i ** 2 == n - 1:
            cnt += 1
        else:
            cnt += 2

res = cnt - 1
for v in div[1:]:
    tmp = n
    while tmp % v == 0:
        tmp //= v
    if tmp % v == 1:
        res += 1

print(res)