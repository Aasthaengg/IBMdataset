import sys
a=input()
b=sys.stdin.read().upper().split().count(a.upper())
print(b)