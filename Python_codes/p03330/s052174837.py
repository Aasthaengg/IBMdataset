import numpy as np
import itertools
import sys
sys.setrecursionlimit(10**9)


INF=10**18
def solve(N,C,D,colormap,new_colormap):
    ans = INF
    for j in range(len(new_colormap)):
        new_colors = new_colormap[j]
        res = 0
        for mod in range(3):
            for current_color in range(1,C+1):
                if current_color == 0: continue
                new_color = new_colors[mod]
                res += D[current_color-1][new_color-1] * colormap[mod][current_color]

        ans = min(res,ans)

    
    print(ans)

    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = [[int(next(tokens)) for _ in range(C)] for _ in range(C)]  # type: "List[List[int]]"
    c = [[int(next(tokens)) for _ in range(N)] for _ in range(N)]  # type: "List[List[int]]"


    colormap = np.zeros((3,C+1),dtype=int)
    for i in range(1,N+1):
        for j in range(1,N+1):
            k = i+j
            k %= 3
            colormap[k][c[i-1][j-1]] += 1
            

    new_color_comb = list(itertools.permutations(list(range(1,C+1)),3))
    solve(N, C, np.array(D), colormap, np.array(new_color_comb))



def cc_export():
    from numba.pycc import CC
    cc = CC('my_module')

    # basic types: https://numba.pydata.org/numba-doc/0.13/types.html
    cc.export('solve', '(i8,i8,i8[:,:],i8[:,:],i8[:,:],)')(solve)
    cc.compile()

if __name__ == '__main__':
    # cc_export()
    try:
        from my_module import solve
    except:
        cc_export()
        exit()

    main()

