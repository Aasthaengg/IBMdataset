import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n=int(input())
    if n==1:
        print('Hello World')
    else:
        a=int(input())
        b=int(input())
        print(a+b)
resolve()