#!/usr/bin/env python3
import sys


def solve(N: int, a: "List[int]"):
    abs_min = 0
    abs_min_index = 0
    for i in range(N):
        if abs(a[i])>abs_min:
            abs_min = abs(a[i])
            abs_min_index = i
    
    print(2*N-1)
    for j in range(1,N+1):
        print(abs_min_index+1,j)

    if a[abs_min_index] >= 0:
        for j in range(1,N):
            print(j,j+1)
    else:
        for j in range(N,1,-1):
            print(j,j-1)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
