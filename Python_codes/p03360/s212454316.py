import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    l=sorted(list(map(int,input().split())))
    k=int(input())
    print(l[2]*2**k+l[0]+l[1])
    
resolve()