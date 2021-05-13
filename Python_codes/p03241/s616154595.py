import sys
input = sys.stdin.readline
from collections import *

def make_divs(n):
    divs = []
    
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            divs.append(i)
            
            if i!=n//i:
                divs.append(n//i)
    
    return divs

N, M = map(int, input().split())
ds = make_divs(M)
ans = 0

for d in ds:
    if M//d>=N:
        ans = max(ans, d)

print(ans)