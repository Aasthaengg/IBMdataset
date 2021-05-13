N=int(input())
ans=[]
n = 55555
primes = set(range(2, n+1))
for i in range(2, int(n**0.5+1)):
    primes.difference_update(range(i*2, n+1, i))
primes=list(primes)
#print(len(primes),primes[:10])
for i in primes:
    if (i%5)==1:
        ans.append(i)
#print(len(ans),ans[:10])
print(*ans[:N])


