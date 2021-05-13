import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():

    [x,y]=list(map(int,input().split()))
    ans=0

    for i in [x,y]:
        if i==1:
            ans+=300000
        elif i ==2:
            ans+=200000
        elif i==3:
            ans+=100000
    if x==1 and y==1:
        ans+=400000
    print(ans)


resolve()