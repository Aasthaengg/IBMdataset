x,y = map(int,input().split())
p = 10**9+7
from math import factorial


if (x+y)%3 != 0:
    print(0)
    exit()



ans = 1
for i in range(0,x//2+2):
    j = x - 2*i
    if 2*j + i == y:
        a = i
        b = j
        break
else:
    print(0)
    exit()

for i in range(1,a+b+1):
    ans *= i%p
    ans %= p
ans %= p

a_inv = 1
for i in range(1,a+1):
    a_inv *= i%p
    a_inv %= p
a_inv = pow(a_inv,p-2,p)

b_inv = 1
for i in range(1,b+1):
    b_inv *= i%p
    b_inv %= p
b_inv = pow(b_inv,p-2,p)

ans *= (a_inv*b_inv)%p

print(ans%p)
