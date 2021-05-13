def divisor(n):
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i * i < n:
                divisors.append(n // i)
        i += 1
    divisors.sort()
    return divisors

N, K = map(int, input().split())
A = list(map(int, input().split()))
divisors = divisor(sum(A))
for d in divisors[::-1]:
    r = [a % d for a in A]
    r.sort(reverse=True)
    i = sum(r) // d
    if sum(r[i:]) <= K:
        print(d)
        exit()