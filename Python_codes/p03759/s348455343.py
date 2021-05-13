import sys

a,b,c = map(int, sys.stdin.readline().split())

if b - a == c - b:
    print("YES")
else:
    print("NO")