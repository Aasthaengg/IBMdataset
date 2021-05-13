import math
n,m=map(int,input().split())
s=input()
t=input()
g = n * m // math.gcd(n, m)

'''if n<m:
    s,t=t,s
    snum,tnum=tnum,snum'''

for i in range(math.gcd(n,m)):
    #print(i, i*(g//m), s[i*(g//m)], i*(g//n), t[i*(g//n)])
    if s[i*(g//m)]!=t[i*(g//n)]:
        print(-1)
        exit()
print(g)