N = int(input())
import math

prime=[]
for n in range(2,55556):
    for i in range(2,math.floor(math.sqrt(n))+1):
        if n % i == 0:
            break
    else:
        if n % 5 == 1:
            prime.append(n)
#print(prime)
#print(len(prime))
print(' '.join(list(map(str, prime[:N]))))
