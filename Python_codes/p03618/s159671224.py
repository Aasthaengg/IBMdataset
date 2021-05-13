import sys
input = sys.stdin.readline
from collections import *

A = input()[:-1]
cnt = defaultdict(int)
ans = 0

for i in range(len(A)):
    ans += i-cnt[A[i]]
    cnt[A[i]] += 1

print(ans+1)