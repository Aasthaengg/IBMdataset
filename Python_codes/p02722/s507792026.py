n = int(input())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

cnt = len(make_divisors(n-1))-1
base = make_divisors(n)
for x in base[1:]:
    org = n
    while org % x == 0:
        org = org / x
    if org % x == 1:
        cnt += 1

print(cnt)