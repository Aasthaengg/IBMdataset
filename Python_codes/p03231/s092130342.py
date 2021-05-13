from math import gcd
def lcm(a,b):
    return a*b//gcd(a,b)
N,M = map(int,input().split())
S = input()
T = input()
g = gcd(N,M)
l = lcm(N,M)
for i in range(g):
    if S[l//M*i] != T[l//N*i]:
        print(-1)
        exit()
print(l)