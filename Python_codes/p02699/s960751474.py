import sys
def input():
    return sys.stdin.readline()[:-1]
S,W = map(int,input().split(' '))
if (S>W):
    print('safe')
else:
    print('unsafe')