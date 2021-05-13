def two_int():
    N, K = map(int, input().split())
    return N,K

def one_int():
    return int(input())

def one_str():
    return input()

def many_int():
    return list(map(int, input().split()))

N, P = two_int()
A=many_int()

even = 0
odd = 0
for a in A:
    if a%2==0:
        even+=1
    else:
        odd+=1

import math
def comb(n,r):
    return math.factorial(n) // (math.factorial(n-r) * math.factorial(r))

even_count=0
for i in range(even+1):
    even_count += comb(even, i)

odd_count=0
if P==1:
    for i in range(1, odd+1, 2):
        odd_count += comb(odd, i)
elif P==0:
    for i in range(2, odd+1, 2):
        odd_count += comb(odd, i)
    odd_count+=1

if odd_count != 0 and even_count != 0:
    print(odd_count * even_count)
else:
    print(odd_count)