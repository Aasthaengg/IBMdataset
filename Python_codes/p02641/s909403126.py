x,n = list(map(int, input().split()))
if n == 0:
    print(x)
else:
    p = list(map(int, input().split()))
    hoge = [i for i in range(x - n, x + n + 1)]
    sabun = list(set(hoge) - set(p))
    min_ = 300
    index_ = 0
    for i, v in enumerate(sabun):
        if abs(x - v) < min_:
            min_ = abs(x - v)
            index_ = i
    print(sabun[index_])