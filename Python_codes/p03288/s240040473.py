import os, sys, re, math

lines = sys.stdin.readlines()

R = int(lines[0])

print ('ABC' if R < 1200 else 'ARC' if R < 2800 else 'AGC')
