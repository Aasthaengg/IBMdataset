import sys,itertools
def input():
    return sys.stdin.readline()[:-1]

N,M = map(int,input().split(' '))
print(N+1-M)