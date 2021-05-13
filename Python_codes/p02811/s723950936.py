import sys
def ISI(): return map(int, sys.stdin.readline().rstrip().split())
k, x = ISI()
if 500*k<x:print("No")
else:print("Yes")