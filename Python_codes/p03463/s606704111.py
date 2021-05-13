import sys
input = lambda: sys.stdin.readline().rstrip()
 
n, a, b = map(int, input().split())

c = b - a

if c % 2 == 1:
    print("Borys")
else:
    print("Alice")
