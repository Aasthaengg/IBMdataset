a,b=map(int, input().split())

if a==1 or b==1:
    print(1)
    exit()

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

a_prime=prime_factorize(a)
b_prime=prime_factorize(b)

a_prime=set(a_prime)
b_prime=set(b_prime)

ans=0
for i in a_prime:
    if i in b_prime:
        ans+=1

print(ans+1)