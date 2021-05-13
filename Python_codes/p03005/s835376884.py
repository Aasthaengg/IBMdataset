# from scipy.sparse import csr_matrix
# import string
import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    n,k=map(int,input().split())
    if k==1:
        print(0)
    else:
        n-=k
        print(n)
    
resolve()