import sys

def S(): return sys.stdin.readline().rstrip()

N,A,B = map(int,S().split())

if (B-A) % 2 == 0:
    print('Alice')
else:
    print('Borys')