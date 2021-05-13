import numpy as np
import sys
sys.setrecursionlimit(10**9)


INF=10**20
def solve(N,P,S,fact):
    ans = 0

    if not 10 % P == 0:
        d = [0] * (P+1)
        s = 0
 
        d[0] = 1
        for i in range(N):
            s += S[N-i-1] * fact[i]
            s %= P
            # s = int(s)
            d[s] += 1
            # print(s)
 
        for m in range(P):
            if d[m] > 0:
                ans += d[m] * (d[m]-1) // 2
 
    else:
        for i in range(N):
            if S[i] % P == 0:
                ans += i+1

 
    return ans

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    S = list(next(tokens))  # type: str

    fact = [pow(10,i,P) for i in range(N)]

    S = list(map(int,S))
    S = np.array(S)
    print(solve(N, P, S,np.array(fact)))


def cc_export():
    from numba.pycc import CC
    cc = CC('my_module')

    # basic types: https://numba.pydata.org/numba-doc/0.13/types.html
    cc.export('solve', '(i8,i8,i8[:],i8[:],)')(solve)
    cc.compile()

if __name__ == '__main__':
    # cc_export()
    try:
        from my_module import solve
    except:
        cc_export()
        exit()

    main()

