from math import sqrt,ceil
S=int(input())

s=ceil(sqrt(S))
adit=pow(s,2)-S
a=0
b=0
#n = int(ceil(sqrt(adit)))
n=ceil(sqrt(adit))
#print(n)
primes = set(range(2, n+1))
for i in range(2, int(n**0.5+1)):
    primes.difference_update(range(i*2, n+1, i))
primes=list(primes)
primes.sort(reverse=True)
primes.append(1)
#print(primes,adit)
for i in primes:
    if adit%i==0:
        a=i
        b=adit//i
        break

#print(s,a,b)
#print(s*s-a*b)
if n==0:
    print(0,0,s,0,0,s)
else:
    print(0,0,a,s,s,b)