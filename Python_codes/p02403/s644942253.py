while True:
    H, W = map(int, input().split())
    if not(H or W):
        break
    while H:
        for i in range(W):
            print('#', end='')
        print()
        H -= 1
    print()