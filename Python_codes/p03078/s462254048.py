# -*- coding: utf-8 -*-
#D - Cake 123
import sys 
from itertools import product
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
X, Y, Z, K = map(int, readline().split())
A = list(map(int,readline().split()))
B = list(map(int,readline().split()))
C = list(map(int,readline().split()))

AB = []
for a,b in product(A,B):
    AB.append(a+b)

AB = sorted(AB,reverse=True)[:K]
ABC = []
for ab,c in product(AB,C):
    ABC.append(ab+c)
ABC = sorted(ABC,reverse=True)

for i in range(K):
    print(ABC[i])