import os, sys, re, math

(H, N) = [int(n) for n in input().split()]
A = [int(n) for n in input().split()]

if sum(A) >= H:
    print('Yes')
else:
    print('No')
