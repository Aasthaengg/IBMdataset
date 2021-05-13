n = int(input())
a = list(map(int,input().split()))
import sys

num = 10**6
li = [0]*num
for k in a:
    li[k-1] += 1

i=2
while i<=num:
    if sum([li[k*i-1] for k in range(1,num//i+1)])>1:
        break
    i+=1
else:
    print("pairwise coprime")
    sys.exit()

import math
import functools
g = functools.reduce(math.gcd,a)
if g==1:
    print("setwise coprime")
    sys.exit()

print("not coprime")
