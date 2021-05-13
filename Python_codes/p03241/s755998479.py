import math
n,m = map(int,input().split())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

divisor_ls = make_divisors(m)

ans = 1
for divisor in divisor_ls:
    if m // divisor < n:
        break
    else:
        ans = divisor

print(ans)