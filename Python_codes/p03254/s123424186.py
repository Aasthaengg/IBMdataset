#!/usr/bin/env python3
import sys


from bisect import bisect_right
import itertools


def solve(N: int, x: int, a: "List[int]"):
    a.sort()
    acum = list(itertools.accumulate(a))
    ans = bisect_right(acum, x)
    if ans == N and acum[-1] < x:
        ans -= 1
    print(ans)
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, x, a)


if __name__ == "__main__":
    main()