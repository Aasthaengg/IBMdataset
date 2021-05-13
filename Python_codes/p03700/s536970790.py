def resolve():
    def f(mid):
        return sum([(x - mid * b + a - b - 1) // (a - b) for x in h if x > mid * b]) <= mid
    n, a, b = map(int, input().split())
    h = [int(input()) for _ in range(n)]
    ok, ng = 10 ** 10, 0
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if f(mid):
            ok = mid
        else:
            ng = mid
    print(ok)


if __name__ == '__main__':
    resolve()
