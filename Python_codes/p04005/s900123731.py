import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():

    L=list(map(int,input().split()))
    prod=L[0]*L[1]*L[2]
    ans=10**20
    for i in L:
        if i%2==0:
            ans= 0
            break
        else:
            ans=min(ans,prod//i)
    print(ans)


resolve()