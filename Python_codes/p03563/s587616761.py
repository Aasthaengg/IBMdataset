import sys, os

f = lambda:list(map(int,input().split()))
if 'local' in os.environ :
    sys.stdin = open('./input.txt', 'r')

def solve():
    r = f()[0]
    g = f()[0]

    print(r + 2*(g-r))

solve()
