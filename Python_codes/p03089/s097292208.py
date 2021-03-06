#!/usr/bin/env python3
import sys


def solve(N: int, b: "List[int]"):
    c = b[:] # debug
    ans = []
    while c:
        x = max(filter(lambda x: x[0] == x[1], enumerate(c, 1)), default=0)
        if not x:
            return [-1]
        ans.append(x[0])
        del c[x[0]-1]
    return ans[::-1]

# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    b = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    print(*solve(N, b), sep="\n")

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
