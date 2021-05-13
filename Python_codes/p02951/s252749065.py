import os, sys, re, math

(A, B, C) = [int(n) for n in input().split()]

print(max(C - (A - B), 0))
