import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n=int(input())
    v=list(map(int,input().split()))
    c=list(map(int,input().split()))
    ans=0
    for x,y in zip(v,c):
        if x-y>0:
         ans+=x-y
    print(ans)
resolve()