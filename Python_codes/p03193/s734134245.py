try:
    n, h, w = map(int, input().split())
    i = 0
    cnt = 0
    while i < n:
        a, b = map(int, input().split())
        if a >= h and b >= w:
            cnt += 1
        i += 1
    print(cnt)
except EOFError:
    pass
