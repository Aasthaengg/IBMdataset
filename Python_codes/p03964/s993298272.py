import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    x,y=1,1
    for _ in range(n):
        a,b=map(int,input().split())
        k=max((x-1)//a+1,(y-1)//b+1)
        x,y=k*a,k*b
    print(x+y)
resolve()