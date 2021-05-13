import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7 # 998244353
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    A=list(map(int,input().split()))
    A.sort()
    print("YES" if(A==[1,4,7,9]) else "NO")
resolve()