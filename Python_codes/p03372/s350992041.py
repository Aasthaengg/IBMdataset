# -*- coding: utf-8 -*-
#D - Static Sushi 
import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N,C = map(int,readline().split())
#時計回りでの距離X,カロリーV
D = []
V = []
for _ in range(N):
    x,v = map(int,readline().split())
    D.append(x)
    V.append(v)
D.append(C)
V.append(0)
##時計回りでのS1-d1,S1-2*d2の最大値 X1,X2
##反時計回りでのS2-d2,S2-2*d2の最大値 Y1,Y2
X1,X2 = [0],[0]
d = 0 
total = 0
tmp1,tmp2 = 0,0
for i in range(N):
    d = D[i]
    total += V[i]
    tmp1 = max(tmp1,total-d)
    tmp2 = max(tmp2,total-2*d)
    X1.append(tmp1)
    X2.append(tmp2)

m1 = 0
m2 = 0
d = 0 
total = 0
for i in range(N,-1,-1):
    d = (C-D[i])
    total += V[i]
    tmp1 = total - d
    tmp2 = total - 2*d
    m1 = max(m1,tmp1+X2[i])
    m2 = max(m2,tmp2+X1[i])
print(max(m1,m2))