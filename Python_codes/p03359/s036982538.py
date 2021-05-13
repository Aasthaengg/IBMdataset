import sys, os

f = lambda:list(map(int,input().split()))
if 'local' in os.environ :
    sys.stdin = open('./input.txt', 'r')

def solve():
    a,b = f()
    if a<=b:
        print(a)
    else:
        print(a-1)


solve()
