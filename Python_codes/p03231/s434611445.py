ma = lambda :map(int,input().split())
ni = lambda:int(input())
import collections
import math
import fractions
gcd = fractions.gcd
n,m = ma()
s = input()
t = input()
l = m*n //gcd(m,n)
ln = []
for i in range(n):
    ln.append((l//n*i+1,s[i]))

for i in range(m):
    ln.append((l//m*i+1,t[i]))
ln.sort()
prev=-1
wp = ""
for num,w in ln:
    if num==prev:
        if w ==wp:
            pass
        else:
            print(-1)
            exit()
    prev=num
    wp = w
print(l)
