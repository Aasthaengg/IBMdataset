from fractions import gcd
import sys
n, m = map(int, input().split())
s = input()
t = input()
if s[0]==t[0]:
    g = gcd(n, m)
    x = g*(n//g)*(m//g)
    num_s, num_t = x//n, x//m
    for i in range(0, x, num_s):
        if i%num_t==0 and s[i//num_s]!=t[i//num_t]:
            print(-1)
            sys.exit()
    print(x)
else:
    print(-1)