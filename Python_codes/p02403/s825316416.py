h,w = [],[]
while True:
    (h,w) = [int(x) for x in input().split()]
    if h == w == 0:
        break
    for x in range(h):
        for y in range(w):
            print('#', end='')
        print()
    print()