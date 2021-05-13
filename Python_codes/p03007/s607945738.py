#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    A.sort()

    if all([a <= 0 for a in A]):
        print(A[-1]-(sum(A)-A[-1]))

        for i in range(N-1):
            print(A[-1],A[i])
            A[-1] -= A[i]
        return
    if all([a >= 0 for a in A]):
        print(sum(A)-A[0]-A[0])
        for i in range(1,N-1):
            print(A[0],A[i])
            A[0] -= A[i]
        print(A[-1],A[0])
        return
    
    answer = 0
    plus = []
    minus = []
    for i in range(N):
        if A[i] >= 0:
            plus.append(A[i])
        else:
            minus.append(A[i])
        answer += abs(A[i])
    print(answer)
    
    while len(plus)>1:
        p = plus.pop()
        m = minus.pop()
        minus.append(m-p)
        print(m,p)
    
    while minus:
        m = minus.pop()
        print(plus[0],m)
        plus[0] -= m
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
