from fractions import gcd
def factor(n):
    res = []
    for i in range(2,int(n**0.5)+1):
        while n % i == 0:
            res.append(i)
            n //= i
    if n > 1:
        res.append(n)
    return res

a,b = map(int,input().split())
c = gcd(a,b)
print(len(set(factor(c)))+1)