import sys
from itertools import combinations_with_replacement, product
import numpy as np
def input(): return sys.stdin.readline().rstrip()

def main():
    N=int(input())
    task=[]
    for _ in range(N):
        A,B=map(int, input().split())
        task.append([A,B])
    task.sort(key=lambda x: x[1])
    task=np.array(task)
    task[:,0]=task[:,0].cumsum()
    if all(task[:,0] <= task[:,1]):
        print('Yes')
    else:
        print('No') 

if __name__ == '__main__':
    main()