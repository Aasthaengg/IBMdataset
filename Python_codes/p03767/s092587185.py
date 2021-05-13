import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():

    N=int(input())
    A=sorted(list(map(int,input().split())))

    ans=0
    for i in range(N,3*N,2):
        ans+=A[i]
    print(ans)
resolve()