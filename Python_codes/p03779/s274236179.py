import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    x=int(input())
    cnt=1
    while cnt*(1+cnt)//2<x:
        cnt+=1
    print(cnt)
resolve()