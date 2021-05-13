import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    a,b=map(int, input().split())
    if a<=8 and b<=8:
        print('Yay!')
    else:
        print(':(')
resolve()