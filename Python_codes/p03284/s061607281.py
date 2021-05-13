import sys 

a,b = map(int, sys.stdin.readline().split())

if a % b == 0:
    print(0)
else:
    print(1)