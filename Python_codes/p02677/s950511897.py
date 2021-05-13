from math import acos,cos,sin
pi = acos(-1)

A,B,H,M=map(int,input().split())

a = (H*60+M)/720*(2*pi)
b = M/60*(2*pi)

posA = A*cos(a),A*sin(a)
posB = B*cos(b),B*sin(b)

print(sum([(posA[i]-posB[i])**2 for i in range(2)])**.5)