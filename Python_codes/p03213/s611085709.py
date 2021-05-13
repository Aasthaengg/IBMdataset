# -*- coding: utf-8 -*-
#D - 756
import sys 
import math
from collections import defaultdict
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N = int(readline())

def prime_factorize(n,cnt):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            while n % i ==0:
                n //= i
                cnt[i] +=1
    if n != 1:
        cnt[n] +=1
    return 

cnt = defaultdict(int)
for i in range(2,N+1):
    prime_factorize(i,cnt)
# n以上の個数を返す
def num(n):
    c = 0
    for v in cnt.values():
        if v < n:
            break
        c += 1
    return c 

print(num(74) + num(24)*(num(2)-1) + num(14)*(num(4)-1) + num(4)*(num(4)-1)*(num(2)-2)//2)           