import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n=int(input())
    l=list(map(int,input().split()))
    wa=sum(l)
    lgu=l[1::2]
    yama1=wa-2*sum(lgu)
    pre=yama1
    print(pre,end=' ')
    for i in range(n-1):
        nextyama=2*l[i]-pre
        pre=nextyama
        print(nextyama,end=' ')
    print()
resolve()