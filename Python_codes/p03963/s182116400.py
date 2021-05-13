import sys
import math
def v():
    n,k=tuple(map(int,sys.stdin.readline().split()))
    res=k*(k-1)**(n-1)
    print(res)
if __name__=='__main__':v()