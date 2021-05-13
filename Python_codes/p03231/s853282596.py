from fractions import gcd
n,m = map(int,input().split())
l = gcd(n,m)
s = input()
t = input()
ok = True
for i in range(l):
    if s[i*n//l] != t[i*m//l]:
        ok = False
print(n*m//l if ok else '-1')