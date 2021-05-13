from itertools import product
import numpy as np
def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    ls = []
    for i in range(N):
        ls.append([A[i], A[i]+1, A[i]-1])
    
    ls = list(product(*ls))
    ans = len(ls)
    for a in ls:
        if np.prod(a) % 2 == 1:
            ans -= 1

    print(ans)

    return

resolve()