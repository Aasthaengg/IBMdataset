import os, sys, re, math

(N, D) = [int(n) for n in input().split()]

w = D * 2 + 1
print((N - 1) // w + 1)
