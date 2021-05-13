import sys
readline = sys.stdin.readline

L,R,d = map(int,readline().split())

print((R // d) - (L - 1) // d)