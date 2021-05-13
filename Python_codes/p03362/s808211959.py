n=int(input())
maxp=55555
primes = set(range(2, maxp+1))
for i in range(2, int(maxp**0.5+1)):
    primes.difference_update(range(i*2, maxp+1, i))
primes=list(primes)
p5=[i for i in primes if i%5==1]
ans=p5[:n]
print(*ans)