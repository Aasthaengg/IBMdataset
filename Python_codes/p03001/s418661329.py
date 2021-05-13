w, h,  x,  y = map(int, input().split())

if h % 2 == 0 and h // 2 == y and w % 2 == 0 and w // 2 == x:
    print('{:.10}'.format(h * w / 2), 1)
else:
    print('{:.10}'.format(h * w / 2), 0)
