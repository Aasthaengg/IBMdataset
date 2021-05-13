import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    k=int(input())
    A=list(map(int,input().split()))

    l=r=2
    for a in A[::-1]:
        l=a*((l-1)//a+1)
        r=a*(r//a)+(a-1)
        if(l>r):
            print(-1)
            return

    print(l,r)
resolve()