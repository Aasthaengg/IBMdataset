import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n=int(input())
    k=int(input())
    ans=1
    for i in range(n):
        ans=min(ans+k,ans*2)
    print(ans)
resolve()