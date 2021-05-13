from math import gcd 

A,B,C,D = map(int,input().split())

Bc = B // C
Bd = B // D

G = gcd(C,D)
L = int(C*D/G)

Bl = B//L

RangeB = B-(Bc+Bd-Bl)

Ac = (A-1) // C
Ad = (A-1) // D
Al = (A-1) // L

RangeA = (A-1)-(Ac+Ad-Al)

print(RangeB-RangeA)