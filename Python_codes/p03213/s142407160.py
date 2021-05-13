import math
from collections import defaultdict
import itertools
def trial_division(n):
    a = [1]
    for i in range(2,int(math.sqrt(n)) + 1):
        while n % i == 0:
            n //= i
            a.append(i)
    a.append(n)
    return a

N = int(input())
d = defaultdict(int)
for i in range(2,N+1):
    for k in trial_division(i):
        if k != 1:
            d[k] += 1
check = []
for v in d.values():
    if v != 1:
        check.append(v)
M = len(check)
tmp = 1
ans = 0

for i in check:
    if i >= 74:
        ans += 1

for i in range(M):
    for k in range(i+1,M):
        for a in range(1,check[i]+1):
            for b in range(1,check[k]+1):
                if (a+1)*(b+1) == 75:
                    ans += 1

for i in range(M):
    for k in range(i+1,M):
        for l in range(k+1,M):
            for a in range(1,check[i]+1):
                for b in range(1,check[k]+1):
                    for c in range(1,check[l]+1):
                        if (a+1)*(b+1)*(c+1) == 75:
                            ans += 1

print(ans)