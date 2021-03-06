#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(A: "List[List[int]]", N: int, b: "List[int]"):
    A_ = []
    for a_ in A:
        A_ += [[a__, False] for a__ in a_]
    for b_ in b:
        for a__ in A_:
            if a__[0] == b_:
                a__[1] = True
    if (A_[0][1] and ((A_[1][1] and A_[2][1]) or \
                        (A_[3][1] and A_[6][1]) or \
                        (A_[4][1] and A_[8][1]))) or \
            (A_[1][1] and A_[4][1] and A_[7][1]) or \
            (A_[2][1] and A_[5][1] and A_[8][1]) or \
            (A_[3][1] and A_[4][1] and A_[5][1]) or \
            (A_[6][1] and A_[7][1] and A_[8][1]) or \
            (A_[2][1] and A_[4][1] and A_[6][1]):
        print(YES)
    else:
        print(NO)
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = [[int(next(tokens)) for _ in range(3)] for _ in range(3)]  # type: "List[List[int]]"
    N = int(next(tokens))  # type: int
    b = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(A, N, b)

if __name__ == '__main__':
    main()
