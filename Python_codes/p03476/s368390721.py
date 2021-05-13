import math
import numpy as np
def get_prime(n):
    if n<= 1:
        return[]
    prime = [2]
    limit = int(math.sqrt(n))
    
    data = [i + 1 for i in range(2,n,2)]
    while limit > data[0]:
        prime.append(data[0])
        data = [j for j in data if j % data[0] != 0]
    return prime + data
def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True
n = int(input())
l = []
r = []
for i in range(n):
    l_, r_ =map(int,input().split())
    l.append(l_)
    r.append(r_)
a = get_prime(10**5+1)
b = np.array([0]*(10**5+2))
c =0
d = 0
add = 0
for i in range(1,len(a)):
    if is_prime((a[i]+1)/2):
        d = a[i] 
        b[c:d] = add 
        c = d
        add +=1
b[c:] = add 
b[0::2] = 0
for i in range(n):
    e = b[max(0, l[i] - 2)]
    f = b[r[i]]
    print(f - e)