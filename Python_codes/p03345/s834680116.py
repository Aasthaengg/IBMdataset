import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    a,b,c,k=map(int, input().split())
    num=0
    if b-a>10**18:
        num='Unfair'
    else:
        if k%2==0:
            num=a-b
        else:
            num=b-a
    print(num)
resolve()