import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    c0=list(map(int,input().split()))
    c1=list(map(int,input().split()))
    c2=list(map(int,input().split()))
    a=[0]*3
    b=[0]*3
    b[0]=c0[0]
    b[1]=c1[0]
    b[2]=c2[0]
    a[1]=c0[1]-b[0]
    a[2]=c0[2]-b[0]
    if a[1]+b[1]==c1[1] and a[1]+b[2]==c2[1] and\
            a[2]+b[1]==c1[2] and a[2]+b[2]==c2[2]:
        print('Yes')
    else:
        print('No')

resolve()