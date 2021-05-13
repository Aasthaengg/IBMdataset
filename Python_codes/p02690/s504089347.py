import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())
def NIJIGEN(H): return [list(input()) for i in range(H)]
X=int(input())
L=list()
R=list()
for i in range(-1000,1001):
  L.append(i**5)
  R.append(i)
for i in range(-1000,1001):
  if (i**5)+X in L:
    n=L.index((i**5)+X)
    print(R[n],i)
    exit()