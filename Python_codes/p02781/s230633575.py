#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)


def solve(N: int, K: int):
    NL = list(map(int, N))

    useMaxDigits = [[0 for i in range(K+1)] for j in range((len(N)+1))]
    noUseMaxDigits = [[0 for i in range(K+1)]
                      for j in range((len(N)+1))]
    useMaxDigits[0][0] = 1
    for digit in range(1, len(N)+1):
        D = NL[digit-1]
        # Use Max continueingly
        if D != 0:
            for i in range(1, K+1):
                useMaxDigits[digit][i] = useMaxDigits[digit-1][i-1]
            for i in range(0, K+1):
                noUseMaxDigits[digit][i] = useMaxDigits[digit-1][i]
        else:
            for i in range(0, K+1):
                useMaxDigits[digit][i] = useMaxDigits[digit-1][i]

        # Use non max
        for i in range(0, K+1):
            # if use zero
            noUseMaxDigits[digit][i] += noUseMaxDigits[digit-1][i]
        for i in range(1, K+1):
            noUseMaxDigits[digit][i] += noUseMaxDigits[digit-1][i-1]*9
        for i in range(1, K+1):
            noUseMaxDigits[digit][i] += useMaxDigits[digit -
                                                     1][i-1]*max(0, D-1)
    print(useMaxDigits[-1][-1]+noUseMaxDigits[-1][-1])
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = next(tokens)  # type: int
    K = int(next(tokens))  # type: int
    solve(N, K)


if __name__ == '__main__':
    main()
