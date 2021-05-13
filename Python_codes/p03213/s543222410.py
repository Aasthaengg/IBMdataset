def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes
N=int(input())
primes=get_primes(N)
numbers=[]
for i in primes:
  temp=0
  j=1
  while i**j<=N:
    temp+=N//(i**j)
    j+=1
  numbers.append(temp)
counter3=0
counter5=0
counter15=0
counter25=0
counter75=0
for i in numbers:
  if i>1:
    counter3+=1
  if i>3:
    counter5+=1
  if i>13:
    counter15+=1
  if i>23:
    counter25+=1
  if i>73:
    counter75+=1
print(counter75+(counter5-1)*counter15+(counter3-1)*counter25+(counter3-2)*(counter5-1)*counter5//2)