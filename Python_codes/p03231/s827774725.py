import fractions
n , m = map(int,input().split())
s = input()
t = input()
l = n*m//fractions.gcd(n,m)
p = l//n
q = l//m

for i in range(10**9):
    if q*i >= n or p*i >= m:
        print(l)
        exit()
    if s[q*i] != t[p*i]:
        print(-1)
        exit()