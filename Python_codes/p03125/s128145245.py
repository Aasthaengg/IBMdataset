import os, sys, re, math

(A, B) = [int(n) for n in input().split()]

if B % A == 0:
    print (A + B)
else:
    print (B - A)
