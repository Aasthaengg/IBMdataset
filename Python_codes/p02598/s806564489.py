# coding: utf-8

def solve(*args: str) -> str:
    n, k = map(int, args[0].split())
    A = tuple(map(int, args[1].split()))

    l, r = 0, max(A)
    while l+1 < r:
        m = (l+r)//2
        cnt = 0
        for a in A:
            cnt += -(-a//m)-1

        if k < cnt:
            l = m
        else:
            r = m

    return str(r)


if __name__ == "__main__":
    print(solve(*(open(0).read().splitlines())))
