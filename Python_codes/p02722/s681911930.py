def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

def make_divisors2(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)

    # divisors.sort()
    return divisors

n=int(input())
l = make_divisors(n-1)
ans = len(l)

l2 = make_divisors2(n)
for i in l2[1:]:
    n1 = n
    while n1%i == 0:
        n1 = n1//i
    if n1%i == 1:
        ans += 1
print(ans)