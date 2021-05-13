import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n=int(input())
    l=list(map(int,input().split()))
    samunenum=100
    samune=10**18
    for i in range(n):
        x=abs(sum(l)-n*l[i])
        if x<samune:
            samunenum=i
            samune=x
    print(samunenum)
resolve()