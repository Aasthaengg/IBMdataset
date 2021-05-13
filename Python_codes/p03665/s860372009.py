#AGC017-A
from math import factorial
def nCr(n,r):
    return factorial(n) / factorial(r) / factorial(n - r)
n,p = map(int,input().split())
a = list(map(int,input().split()))
even = 0
odd = 0
for i in a:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

#偶数
if p == 0:
    temp = 0
    for i in range(0,odd+1,2):
        temp += nCr(odd,i)
    print(int(2**even * temp))
#奇数
else:
    temp = 0
    for i in range(1,odd+1,2):
        temp += nCr(odd,i)
    print(int(2**even * temp))