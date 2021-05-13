def rect(h, w):
    while h > 0:
        print('#' * w)
        h -= 1
    print()
    return

while True:
    n = list(map(int, input().split()))
    H = n[0]
    W = n[1]
    if (H == 0 and W == 0):
        break
    rect(H, W)