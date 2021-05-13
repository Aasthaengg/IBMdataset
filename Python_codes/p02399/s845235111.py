import sys

def solve():
    a,b = map(int,input().split())
    print(int(a//b), a%b, "%f" % (a/b))
    
solve()
