#!/usr/bin/env python3
import sys
import heapq

YES = "Yes"  # type: str
NO = "No"  # type: str

def isBlock(S,i):
    return S[i] == "#"

def hasContinuingSharp(S,A,B):
    prevSharp = False
    for i in range(A,B):
        if isBlock(S,i):
            if prevSharp:
                return True
            else:
                prevSharp = True
        else:
            prevSharp = False
    return False

def hasThreeContinueingNonSharp(S,A,B):
    nonBlockCount = 0
    for i in range(A,B):
        if isBlock(S,i):
            nonBlockCount = 0
        else:
            nonBlockCount += 1
            if nonBlockCount == 3:
                return True
    return False

def solve(N: int, A: int, B: int, C: int, D: int, S: str):
    A-=1
    B-=1
    C-=1
    D-=1
    if hasContinuingSharp(S,A,C) or hasContinuingSharp(S,B,D):
        print(NO)
        return
    if C < D:
        print(YES)
        return
    if hasThreeContinueingNonSharp(S,B-1,D+2):
        print(YES)
    else:
        print(NO)
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, A, B, C, D, S)

if __name__ == '__main__':
    main()