import numpy as np
n=int(input())
d=np.zeros(101)
def factorization(n):
    temp = n
    for i in range(2, int(n**0.5)+1):
        if temp%i==0:
            while temp%i==0:
                d[i]+=1
                temp //= i
    if temp!=1:
        d[temp]+=1
def cnt(k):
    return len(d[d>=k])
for i in range(2,n+1):
    factorization(i)
print(cnt(74)+cnt(24)*(cnt(2)-1)+cnt(14)*(cnt(4)-1)+cnt(4)*(cnt(4)-1)*(cnt(2)-2)//2)