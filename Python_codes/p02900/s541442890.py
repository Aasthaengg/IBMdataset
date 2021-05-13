import fractions
a,b=map(int,input().split())
g=fractions.gcd(a,b)

def prime_factor(n):
    ass = set() 
    for i in range(2,int(n**0.5)+1):
        while n % i==0:
            ass.add(i)
            n = n//i
    if n != 1:
        ass.add(n)
    return ass

print(len(prime_factor(g))+1)