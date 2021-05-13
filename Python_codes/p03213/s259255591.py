from collections import defaultdict
import numpy as np
from itertools import permutations, combinations
n=int(input())
d=defaultdict(int)
def factorization(n):
    temp = n
    for i in range(2, int(n**0.5)+1):
        if temp%i==0:
            while temp%i==0:
                d[i]+=1
                temp //= i

    if temp!=1:
        d[temp]+=1
for i in range(2,n+1):
    factorization(i)
d=np.array(list(d.values()))
ans=0
ans+=len(d[d>=74])
d1=d[d>=2]
d2=d[d>=4]
for x,y in permutations(d1,2):
    if y>=24:
        ans+=1
for x,y in permutations(d2,2):
    if y>=14:
        ans+=1
ans1=0
for x,y,z in permutations(d1,3):
    if y>=4 and z>=4:
        ans1+=1
print(ans+ans1//2)