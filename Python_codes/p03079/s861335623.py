import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    a,b,c=map(int, input().split())
    if a==b==c:
        print('Yes')
    else:
        print('No')
resolve()