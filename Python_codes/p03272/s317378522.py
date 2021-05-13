import os, sys, re, math

lines = sys.stdin.readlines()

(N, i) = [int(i) for i in lines[0].split()]

print (N + 1 - i)
