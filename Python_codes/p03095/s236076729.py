import sys
input = lambda : sys.stdin.readline().rstrip()
mod = 10**9 + 7

n = int(input())
s = input()
from collections import Counter
c = Counter(s)
ans = 1
for i in c:
    ans *= c[i] + 1
    ans %= mod
ans -= 1
print(ans)        

