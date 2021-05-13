def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

n, k = map(int, input().split())
mod = 10**9 + 7

lst = [0 for i in range(k+1)]
for i in range(1, k+1)[::-1]:
    num = pow(k//i, n, mod)
    lst[i] += num
    divisors = make_divisors(i)
    for j in divisors:
        if j != i: lst[j] -= lst[i]

ans = 0
for i in range(1, k+1):
    ans = (ans + i*lst[i]) % mod
print(ans)