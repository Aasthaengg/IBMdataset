import sys

def yn(b):
    print("Yes" if b==1 else "No")
    return

def resolve():
    readline=sys.stdin.readline
    x=int(readline().strip())
    if x<1200:
        print("ABC")
    else:
        print("ARC")
    #n,m,k=list(map(int, readline().strip().split()))
    #arr=list(map(int, readline().strip().split()))
    #n=int(readline().strip())
    #yn(1)

    return


resolve()
