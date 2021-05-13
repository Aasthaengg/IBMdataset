#!/usr/bin/env python3
import sys
from pprint import pprint

def solve(N: int, A: "List[int]"):
    bits = [[] for _ in range(N)]
    for i, a in enumerate(A):
        bit = 0
        while a > 0:
            if a % 2 == 1:
                bits[i].append(bit)
            a //= 2
            bit += 1
    #pprint(bits)
    cur = set()
    l = 0
    r = 0
    ret = 0
    while l < N:
        while r < N:
            ok = True
            for b in bits[r]:
                if b in cur:
                    ok = False
            if ok:
                for b in bits[r]:
                    cur.add(b)
                r += 1
            else:
                break
        ret += r - l
        #print(l, r)
        for b in bits[l]:
            cur.remove(b)
        l += 1
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
