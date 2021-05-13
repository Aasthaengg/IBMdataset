import sys

def yn(b):
    print("Yes" if b==1 else "No")
    return

def resolve():
    readline=sys.stdin.readline
    a,b,x=map(int, readline().rstrip().split())
    print(b//x - (a-1)//x)
    return

if 'doTest' not in globals():
    resolve()
    sys.exit()