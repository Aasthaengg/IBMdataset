import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    a,b=map(int, input().split())
    if a%3==0 or b%3==0 or (a+b)%3==0:
        print('Possible')
    else:
        print('Impossible')
resolve()