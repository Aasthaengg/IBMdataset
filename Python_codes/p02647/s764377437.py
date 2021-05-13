import sys
import numpy as np
from numba import njit, i8
input = lambda: sys.stdin.readline().rstrip()

@njit(i8[:](i8[:]), cache=True)
def count(a):
    tmp = np.zeros_like(a)
    for index, num in enumerate(a):
        left = max(0, index-num)      
        right = min(len(a)-1, index+num)  
        tmp[left] += 1              
        if right + 1 < len(a):
            tmp[right + 1] -= 1
    tmp = np.cumsum(tmp)
    return tmp

def main():
    n, k = map(int, input().split())
    a = np.array(list(map(int, input().split())))
    for _ in range(k):
        a = count(a)
        if len(set(a)) == 1 and n in set(a):
            print(*a)
            return
    print(*a)

if __name__ == '__main__':
    main()