while True:
    [H, W] = [int(x) for x in raw_input().split()]
    if [H, W] == [0, 0]:
        break
    print('#' * W)
    counter = 0
    while counter < H - 2:
        print('#' + '.' * (W - 2) + '#')
        counter += 1
    print('#' * W + '\n')