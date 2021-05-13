import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    a=int(input())
    b=int(input())
    h=int(input())
    print(((a+b)*h)//2)
resolve()