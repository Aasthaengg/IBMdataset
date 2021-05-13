n = int(input())

def make_div(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

divs = make_div(n)
ans=0
for r in divs:
    m=n//r -1
    if r<m:
        ans+=m
print(ans)