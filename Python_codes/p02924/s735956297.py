import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n=int(input())
    print((1+n)*n//2-n)
resolve()