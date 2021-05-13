import numpy as np
import sys
sys.setrecursionlimit(10**9)


INF=10**18

def solve(N,A):
    maxim = 10**6+10
    spf = np.zeros(maxim+1,dtype=np.int64)

    # osa_k 
    for i in range(maxim):
        spf[i] = i
    
    i = 2
    while i*i <= maxim:
        if spf[i] != i: i += 1; continue
        j = i*i
        while j <= maxim:
            if spf[j] != j: j += i; continue
            spf[j] = i
            j += i
        
        i += 1

    pairwise = True
    allP = set()
    for a in A:

        m  = set()
        n = a
        while n > 1:
            m.add(spf[n])
            n //= spf[n]

        P = m

        no_collapse = len(allP) + len(P)
        for p in P:
            allP.add(p)
        
        res = len(allP)
        if no_collapse != res:
            pairwise = False
            break


    return pairwise

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"

    pairwise = solve(N, np.array(A))

    if pairwise:
        print("pairwise coprime")
    else:
        gcm = np.gcd.reduce(A)
        if gcm == 1:
            print("setwise coprime")
        else:
            print("not coprime")


def cc_export():
    from numba.pycc import CC
    cc = CC('my_module')

    # basic types: https://numba.pydata.org/numba-doc/0.13/types.html
    cc.export('solve', '(i8,i8[:],)')(solve)
    cc.compile()

if __name__ == '__main__':
    # cc_export()
    try:
        from my_module import solve
    except:
        cc_export()
        exit()

    main()


