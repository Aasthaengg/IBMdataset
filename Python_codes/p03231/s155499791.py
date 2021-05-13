#!/usr/bin/env python3
import sys
import fractions

## 最小公倍数(LCM)
def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

def solve(N: int, M: int, S: str, T: str):
    X = lcm(N,M)
    i = j = 0

    while i < N and j < M:
        if S[i] == T[j]:
            i += X//M
            j += X//N
            continue
        else:
            print(-1)
            return
    print(X)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    T = next(tokens)  # type: str
    solve(N, M, S, T)

if __name__ == '__main__':
    main()
