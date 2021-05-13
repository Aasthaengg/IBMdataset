import os, sys, re, math

(a, b) = [int(n) for n in input().split()]

if a > b:
    print(str(b) * a)
else:
    print(str(a) * b)
