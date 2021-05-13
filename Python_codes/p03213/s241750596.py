n = int(input())
import  numpy as np
fact = np.zeros(100)
def prime_factorize(n):
    while n % 2 == 0:
        fact[1]+=1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            fact[f-1] += 1
            n //= f
        else:
            f += 2
    if n != 1:
        fact[n-1] += 1

for i in range(2, n + 1):
  prime_factorize(i)

def num(a):
  return sum(fact>=a-1)

print(num(75) + num(25)*(num(3)-1) + num(15)*(num(5)-1) + num(5)*(num(5)-1)*(num(3)-2)//2)