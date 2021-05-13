import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n,c,k=map(int, input().split())
    l=[int(input()) for i in range(n)]
    l.sort()
    saisyo=l[0]
    ninzu=1
    ans=0
    for j in range(1,n):
        x=l[j]-saisyo
        if x<=k and ninzu<c:
            ninzu+=1
        else:
            ans+=1
            saisyo=l[j]
            ninzu=1
    print(ans+1)
resolve()