import sys

def input():
    return sys.stdin.readline()[:-1]


x = int(input())

if x == 0:
    print(1)
else:
    print(0)
