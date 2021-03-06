#!/usr/bin/env python3
import sys


def solve(H: int, W: int, c: "List[List[int]]", A: "List[List[int]]"):
    #print(*c, sep='\n')
    for k in range(10):
        for i in range(10):
            for j in range(10):
                c[i][j] = min(c[i][j], c[i][k]+c[k][j])
    #print(*c, sep='\n')
    cost = 0
    for a in A:
        for aa in a:
            if aa == -1:
                continue
            cost += c[aa][1]
    return cost


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    c = [[int(next(tokens)) for _ in range(9 - 0 + 1)] for _ in range(9 - 0 + 1)]  # type: "List[List[int]]"
    A = [[int(next(tokens)) for _ in range(W)] for _ in range(H)]  # type: "List[List[int]]"
    print(solve(H, W, c, A))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
