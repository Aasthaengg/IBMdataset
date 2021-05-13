m, k = map(int, input().split())

if k >= 2**m:
    print(-1)
elif m == 1:
    if k == 0:
        print("0 0 1 1")
    elif k == 1:
        print(-1)
else:
    l = list(range(2**m))
    l.remove(k)
    ret = l + [k] + l[::-1] + [k]
    print(*ret)
