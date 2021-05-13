import sys

def I(): return int(sys.stdin.readline().rstrip())

N = I()

print(((N+1)//2)/N)