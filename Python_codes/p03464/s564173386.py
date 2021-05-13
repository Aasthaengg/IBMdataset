# binary_search

def is_ok(x, f):
    for d in a:
        x = x - x % d
    return f(x)


def binary_search(f, ok, ng):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid, f):
            ok = mid
        else:
            ng = mid
    return ok


k = int(input())
a = tuple(map(int, input().split()))

max_ = binary_search(lambda x: x <= 2, ok=0, ng=10 ** 14 + 10)
min_ = binary_search(lambda x: x >= 2, ok=10 ** 14 + 10, ng=0)

if min_ > max_:
    print(-1)
else:
    print(min_, max_)
