#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, A: int, B: int, v: "List[int]"):
    def choose(n, k):
        ret = 1
        k = min(k, n - k)
        for i in range(1, k + 1):
            ret *= (n - i + 1)
            ret //= i
        return ret

    count = {}
    v.sort(reverse=True)
    ave = [0] * N
    for val in v:
        if val in count:
            count[val] += 1
        else:
            count[val]  = 1
    for i in range(A - 1, B):
        ave[i] = sum(v[:i + 1]) / (i + 1)
    mx = max(ave)

    ret = 0
    for i in range(A - 1, B):
        if ave[i] == mx:
            c = 0
            for j in range(i + 1, N):
                if v[j] == v[i]:
                    c += 1
            ret += choose(count[v[i]], c)
    print(mx)
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    v = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, A, B, v)

if __name__ == '__main__':
    main()
