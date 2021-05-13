import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n=int(input())
    ans=10**18
    for i in range(1,n):
        x=sum([int(j) for j in str(i)])+sum([int(j) for j in str(n-i)])
        ans=min(ans,x)
    print(ans)
resolve()