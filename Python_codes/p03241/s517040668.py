def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


N, M = map(int, input().split())

Mlist = make_divisors(M)

ans = 0
for i in Mlist:
    if N * i <= M:
        ans = i
    else:
        break

print(ans)