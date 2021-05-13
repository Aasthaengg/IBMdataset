import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    from itertools import accumulate

    N = int(input())  # len(A)
    A = list(map(int, input().split()))
    zenbu=sum(A)
    B = [0] + A
    B = list(accumulate(B))
    C = [zenbu]*(N+1)
    import numpy as np
    B=np.array(B)
    C=np.array(C)
    D=C-B
    ans=10**18
    for i in range(1, N):
        ans = min(abs(B[i]-D[i]),ans)
    print(ans)
resolve()