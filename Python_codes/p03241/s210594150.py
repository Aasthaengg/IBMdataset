def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


n,m=map(int,input().split())

mlis=make_divisors(m)

I=1
for i in mlis:
    if m<i*n:
        break
    else:
        I=i
    
print(I)