import sys, os

f = lambda:list(map(int,input().split()))
if 'local' in os.environ :
    sys.stdin = open('./input.txt', 'r')

def solve():
    a,b = f()
    print(max(a+b, a-b, a*b))

solve()
