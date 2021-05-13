import sys
import os
import math

A,B,K=map(int, input().split())

C = min(A, B)
hairetu = []

for i in range(1, C+1):
    if A % i == 0 and B % i == 0:
        hairetu.append(i)

print(hairetu[-K])