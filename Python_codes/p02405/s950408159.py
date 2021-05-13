while True:
    h,w = map(int,input().split())
    if w == 0 and h == 0:
        break
    for j in range(h):
        for i in range(w):
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()