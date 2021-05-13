import sys
import numpy as np
def input(): return sys.stdin.readline().rstrip()

def main():
    A=int(input())
    B=int(input())
    C=int(input())
    X=int(input())
    arr=np.add.outer(np.arange(0,100*B+1,100).T,np.arange(0,500*A+1,500))
    arr= X-arr
    print(arr[(arr>=0) & (arr<=50*C)].size)

if __name__ == '__main__':
    main()