# -*- coding: utf-8 -*-
import sys

N,M = list(map(int, input().rstrip().split()))
S = input().strip()
T = input().strip()
#-----

def gcd(a,b):
    if b == 0: 
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

lcm = lcm(N,M)
L = lcm
X1_dic={}

X1_dic[0] = S[0]
for i in range(1,N):
    X1_dic[ int(i*(L/N)+1) - 1 ] = S[i]


if X1_dic[0] != T[0]:
    print(-1)
    sys.exit()

for i in range(1,M):
    key = int(i*(L/M)+1) - 1
    if (key in X1_dic) and  X1_dic[key] != T[i]:
        print(-1)
        sys.exit()
    
print(L)
