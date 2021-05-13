import os, sys, re, math

lines = sys.stdin.readlines()

(N, K) = [int(i) for i in lines[0].split()]

print ('0' if N % K == 0 and N >= K else '1')
