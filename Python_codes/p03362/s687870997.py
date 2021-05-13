import math
# isprime, prime_division
from sys import stdout
printn = lambda x: stdout.write(str(x))
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 999999999
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

def isprime(x):
    q = int(math.sqrt(x))  # int() rounds to zero
    for i in range(2,q+1):   # upto q
        if x%i == 0:
            return False
    return True

def prime_division(x):
    q = int(math.sqrt(x))
    a = []
    for i in range(2,q+1):
        ex = 0
        while x%i == 0:
            ex += 1
            x //= i
        if ex>0:
            a.append([i,ex])
    if x>q:
        a.append([x,1])
    return a

def divisorlist(z): # z : output of prime_division
    if len(z)==1:
        return [z[0][0]**i for i in range(z[0][1]+1)]
    y = divisorlist(z[1:])
    s = []
    for i in range(z[0][1]+1):
        for j in y:
            s.append((z[0][0]**i)*j)
    return s

n = inn()
p = []
for i in range(11,55555,5):
    if isprime(i):
        p.append(i)
        if len(p)==n:
            break

pad = ''
for x in p:
    printn(pad + str(x))
    pad = ' '
print("")
