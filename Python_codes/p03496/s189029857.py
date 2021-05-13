#!/usr/bin/env python3
import sys
INF = float("inf")


def argmax(a):
    index, value = -1, -float("inf")
    for i, v in enumerate(a):
        if value < v:
            index, value = i, v
    return index, value


def argmin(a):
    index, value = -1, float("inf")
    for i, v in enumerate(a):
        if value > v:
            index, value = i, v
    return index, value


def solve(N: int, a: "List[int]"):
    # 正のみからなる数列に直す
    amin_arg, amin = argmin(a)
    amax_arg, amax = argmax(a)
    ans = []
    if abs(amin) <= abs(amax):
        for i in range(N):
            if a[i] < 0:
                ans.append([amax_arg+1, i+1])
                a[i] += amax
        # すべて0以上の要素の数列となった
        # print(a)
        # 累積和の要領
        for i in range(N-1):
            if a[i] > a[i+1]:
                ans.append([i+1, i+2])
                a[i+1] += a[i]
        # print(a)

    else:
        for i in range(N):
            if a[i] > 0:
                ans.append([amin_arg+1, i+1])
                a[i] += amin
        # すべて0以下の要素の数列となった。
        # print(a)
        # 累積和の要領
        for i in range(N-1, 0, -1):
            if a[i-1] > a[i]:
                ans.append([i+1, i])
                a[i-1] += a[i]
        # print(a)
    print(len(ans))
    for a in ans:
        print(*a)
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
