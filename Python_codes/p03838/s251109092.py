import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():

    x,y=map(int,input().split())
    ans=10**20
    if -x<=-y:
        ans=min(ans,2+-y-(-x))
    if -x<=y:
        ans=min(ans,1+y-(-x))
    if x<=-y:
        ans=min(ans,1+(-y)-x)
    if x<=y:
        ans=min(ans,y-x)
    print(ans)

resolve()