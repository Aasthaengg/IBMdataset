import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n=int(input())
    l=list(map(int,input().split()))
    l2=sorted(l)
    x=l2[n//2-1]
    y=l2[n//2]
    if x==y:
        for i in range(n):
            print(x)
    else:
        setx=set(l2[:n//2])
        sety=set(l2[n//2:])
        for i in l:
            if i in setx:
                print(y)
            else:
                print(x)
resolve()