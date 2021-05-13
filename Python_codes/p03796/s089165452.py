import sys
import math
import itertools
MOD=10**9+7
n = int(input())
ans=1
for i in range(1, n + 1):
    ans =ans%MOD*i
print(ans%MOD)