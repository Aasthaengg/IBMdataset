while True:
    h, w = [int(x) for x in input().split()]
    if h == w == 0:
        break
    for i in range(h):
        print('#' * w)
    print()