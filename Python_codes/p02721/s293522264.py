#!/usr/bin/env python3
import sys


def solve(N: int, K: int, C: int, S: str):
    l = [None] * N
    r = [None] * N

    pre = -float('inf')
    k = -1
    for cur in range(N):
        if cur - pre > C and S[cur] == 'o':
            k += 1
            pre = cur
            l[k] = cur

    pre = float('inf')
    k = K
    for cur in range(N-1, -1, -1):
        if pre - cur > C and S[cur] == 'o':
            k -= 1
            pre = cur
            r[k] = cur

    return [ll+1 for ll, rr in zip(l[:K], r[:K]) if ll == rr]
    


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    print(*solve(N, K, C, S), sep='\n')

if __name__ == '__main__':
    main()
