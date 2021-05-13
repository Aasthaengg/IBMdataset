import os, sys, re, math

N = int(input())
(S, T) = [n for n in input().split()]

print(''.join(['%s%s' % (x, y) for (x, y) in zip(S, T)]))
