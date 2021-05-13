from math import *

def lcm(a,b):
    return a*b//gcd(a,b)

def lcm2(array):
    temp = 1
    for a in array:
        temp = lcm(temp, a)
    return temp

N, M = map(int, input().split())
A = list(map(int, input().split()))
A = list(map(lambda x:x//2, A))

b = []
for a in A:
    cnt = 0
    while a:
        if not a%2:
            cnt += 1
            a = a // 2
        else:
            break
    b.append(cnt)

if b.count(cnt) != N:
    print(0)
    exit()

res = lcm2(A)

print((M//res-1)//2+1)