def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

ans=0
n = int(input())
divisors = make_divisors(n)
for i in divisors[1:]:
    i -= 1
    if n % i == n//i:
        ans += i

print(ans)