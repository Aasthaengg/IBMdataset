from sys import stdin, stdout
from time import perf_counter

import sys
sys.setrecursionlimit(10**9)
mod = 10**9+7




s = input()

print("Bad" if s[0]==s[1] or s[1]==s[2] or s[2]==s[3] else "Good")