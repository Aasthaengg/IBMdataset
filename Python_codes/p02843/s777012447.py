import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    x=int(input())
    a,b=divmod(x,100)
    if x<100:
        print(0)
    elif b<=a*5:
        print(1)
    else:
        print(0)
resolve()