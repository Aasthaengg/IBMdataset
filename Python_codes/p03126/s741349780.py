#

import sys
from copy import deepcopy
input=sys.stdin.readline

def main():
    N,M=map(int,input().split())
    sukic=[0]*(M+1)
    for i in range(N):
        A=list(map(int,input().split()))
        for j in range(A[0]):
            sukic[A[j+1]]+=1
    print(sukic.count(N))
    
if __name__=="__main__":
    main()
