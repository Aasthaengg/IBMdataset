import sys
readline = sys.stdin.readline

A,B,C = map(int,readline().split())

print(max(0,C - (A - B)))
