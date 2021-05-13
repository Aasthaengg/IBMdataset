import sys
from itertools import combinations_with_replacement, product
import numpy as np
def input(): return sys.stdin.readline().rstrip()


def main():
    n, m, x = map(int, input().split())
    data = np.zeros((n,m+1),int)
    ans=10**10
    for i in range(n):
        data[i]=np.array(list(map(int, input().split())))
    for bit in list(product([0,1],repeat=n)):
        calc=np.dot(np.array(bit), data)
        if all(calc[1:]>=x):
            ans=min(ans,calc[0])
    
    if ans==10**10:
        print(-1)
    else:
        print(ans)




if __name__ == '__main__':
    main()