q=int(input())
lr=[list(map(int, input().split())) for _ in range(q)]

import math
def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

n=10**5+1
prime_list=[0]*n
for i in range(3,n,1):
    if is_prime(i) and is_prime((i+1)//2):
        prime_list[i]=1

from itertools import accumulate
acc=list(accumulate(prime_list))

for lr_i in lr:
    print(acc[lr_i[1]]-acc[lr_i[0]-1])

