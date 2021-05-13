while True:
    h, w = map(int,input().split())
    if h == 0 and w ==0:
        break

    else:
        print('#'*w)

        h2 = h-2
        w2 = w-2
        for i in range(0, h2):
            print('#' + '.'*w2 + '#')
        print('#'*w)
        print('')