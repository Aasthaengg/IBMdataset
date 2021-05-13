import sys

def yn(b):
    print("Yes" if b==1 else "No")
    return

def resolve():
    readline=sys.stdin.readline

    a,b,c,d=list(map(int, readline().strip().split()))
    print(max(a*b,c*d))

    return


resolve()