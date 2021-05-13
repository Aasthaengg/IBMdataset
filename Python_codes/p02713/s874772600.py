from math import gcd
r = range(1, int(input()) + 1)
print(sum(gcd(gcd(i,j),k) for i in r for j in r for k in r))