H, W = map(int, input().split())
while H or W:
    print('#' * W)
    for i in range(H-2):
        print('#' + '.' * (W - 2) + '#')
    print('#' * W, end='\n\n')
    H, W = map(int, input().split())