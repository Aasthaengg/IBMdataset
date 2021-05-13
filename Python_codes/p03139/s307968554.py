import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n,a,b=map(int, input().split())
    ans1=min(a,b)
    ans2=max(a+b-n,0)
    print(ans1,ans2)
resolve()