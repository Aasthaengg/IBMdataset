n=int(input())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

divs=make_divisors(n)
ans=0
for div_i in divs:
    k=div_i
    m=(n-k)//k
    if m>k:
        ans+=m
print(ans)
