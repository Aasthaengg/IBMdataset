while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    for i in range(h):
        if i % 2 == 0:
            if w % 2 == 0:
                print('#.'*(w//2))
            else:
                print('#.'*((w-1)//2)+'#')
        else:
            if w % 2 == 0:
                print('.#'*(w//2))
            else:
                print('.#'*((w-1)//2)+'.')
    print()

