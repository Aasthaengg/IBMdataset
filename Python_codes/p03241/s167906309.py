N, M = map(int, input().split())
ans = 1

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


A = make_divisors(M)
for an, a in zip(A, A[1:]):
    ans = an
    if a * N > M:
        break
else:
    ans = M
print(ans)