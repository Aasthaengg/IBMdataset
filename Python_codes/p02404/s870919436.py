h,w = [],[]
while True:
    (h,w) = [int(x) for x in input().split()]
    if h == w == 0:
        break
    for x in range(h):
        for y in range(w):
            if x == 0 or y == 0 or x == h-1 or y == w-1:
                print('#',end='')
            else:
                print('.', end='')
        print()
    print()