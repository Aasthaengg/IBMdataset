import math
import sys
n, m = map(int, input().split())
s = list(input())
t = list(input())
a = (n*m)//math.gcd(n, m)
b0 = [i*(a//n)+1 for i in range(n)]
b1 = [i*(a//m)+1 for i in range(m)]
b2 = set(b0)
b3 = set(b1)

for j, i in enumerate(b0):
    if i in b3:
        if s[j] != t[b1.index(i)]:
            print(-1)
            sys.exit()
            
for j, i in enumerate(b1):
    if i in b2:
        if s[b0.index(i)] != t[j]:
            print(-1)
            sys.exit()
print(a)
