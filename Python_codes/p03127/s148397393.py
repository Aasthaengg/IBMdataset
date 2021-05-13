from fractions import gcd
n = int(input())
a = list(map(int,input().split()))
c = 0
for i in a:
    c = gcd(c,i) 
print(c)