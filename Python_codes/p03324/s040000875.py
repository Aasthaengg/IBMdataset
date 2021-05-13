import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    d,n=map(int, input().split())
    if n!=100:
        print(100**d*n)
    elif n==100:
        print(100**d*101)
resolve()
