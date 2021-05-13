#!/usr/bin/env python3


def _f(H, W, S):
    '''
    >>> f = _f(3, 3, [[1, 0, 0], [1, 0, 1], [0, 1, 1]])
    >>> f(0, 0, 1, 1)
    1
    >>> f(0, 0, 3, 0)
    0
    >>> f(0, 0, 3, 1)
    2
    >>> f(1, 1, 3, 3)
    3
    >>> f(0, 0, 3, 3)
    5
    >>> f(2, 0, 3, 3)
    2
    '''
    acc = [[0] * (W + 1) for _ in range(H+1)]
    for h in range(1, H+1):
        for w in range(1, W+1):
            acc[h][w] = acc[h][w-1] + acc[h-1][w] - acc[h-1][w-1] + S[h-1][w-1]

    def f(sh, sw, eh, ew):
        return acc[eh][ew] + acc[sh][sw] - acc[sh][ew] - acc[eh][sw]

    return f

def _solve(H, W, K, S, c, f):
    #print(H, W, K, S, c, f)
    sw = 0
    cut = 0
    for ew in range(1, W+1):
        #print([(((sh, sw), (eh, ew)), f(sh, sw, eh, ew)) for sh, eh in c])    
        if any(f(sh, ew-1, eh, ew) > K for sh, eh in c):
            return float('inf')
        if any(f(sh, sw, eh, ew) > K for sh, eh in c):
            cut += 1
            sw = ew - 1
    return cut


def solve(H, W, K, S):
    from itertools import product, compress
    f = _f(H, W, S)
    ans = float('inf')
    for flag in product(range(2), repeat=H-1):
        t = (0,) + tuple(compress(range(1,H), flag)) + (H,)
        c = tuple(zip(t, t[1:]))
        ans = min(ans, _solve(H, W, K, S, c, f)+sum(flag))
    return ans


    

# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools
def main():
    H, W, K = list(map(int, input().split()))
    S = [list(map(int, input())) for _ in range(H)]
    print(solve(H, W, K, S))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()