import math
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

a,b,c=map(int,input().split())
n=math.gcd(a,b)
ans=make_divisors(n)
print(ans[-c])