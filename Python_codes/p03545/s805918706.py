import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

A = list(map(int,sys.stdin.readline().rstrip()))

from itertools import product

X = ['+','-']
for a in product(X,repeat=3):
    b = A[0]
    for i in range(3):
        if a[i] == '+':
            b += A[i+1]
        else:
            b -= A[i+1]
    if b == 7:
        print(str(A[0])+a[0]+str(A[1])+a[1]+str(A[2])+a[2]+str(A[3])+'=7')
        break
