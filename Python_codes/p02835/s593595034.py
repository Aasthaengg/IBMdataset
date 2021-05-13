import sys
input=sys.stdin.readline
def N(): return int(input())
def NM():return map(int,input().split())
def L():return list(NM())
def LN(n):return [N() for i in range(n)]
def LL(n):return [L() for i in range(n)]
l=L()
if sum(l)<=21:
    print("win")
else:
    print("bust")