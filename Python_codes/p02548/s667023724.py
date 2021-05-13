def N():
    return int(input())
def L():
    return list(map(int,input().split()))
def NL(n):
    return [list(map(int,input().split())) for i in range(n)]
mod = pow(10,9)+7
#import numpy
#import sympy
import math
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
def divi(n):
    ans = {1}
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            ans |= l[i]
            ans |= l[n//i]
    ans.add(n)
    return ans

n = N()
cnt = 1
l = [{} for _ in range(n)]
l[1] = {1}
tab = [0]*(n+1)
for i in range(1,n+1):
    for j in range(i, n + 1, i):
        tab[j] += 1
tab[n]=0
print(sum(tab))