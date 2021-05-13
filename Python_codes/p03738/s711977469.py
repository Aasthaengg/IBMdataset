import sys
input = sys.stdin.readline
A = int(input())
B = int(input())
if A < B: print("LESS")
elif A == B: print("EQUAL")
else: print("GREATER")
