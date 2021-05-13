import sys, os

f = lambda:list(map(int,input().split()))
if 'local' in os.environ :
    sys.stdin = open('./input.txt', 'r')

def solve():
    a,b,c = f()
    if c>=a and c<=b:
        print('Yes')
    else:
        print('No')

solve()
