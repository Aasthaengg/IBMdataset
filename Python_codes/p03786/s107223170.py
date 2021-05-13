import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    N=int(input())
    A=sorted(list(map(int,input().split())))

    tot=0
    maxind=-1
    for i in range(N-1):
        tot+=A[i]
        if tot*2<A[i+1]:
            maxind=i
    print(N-(maxind+1))


resolve()