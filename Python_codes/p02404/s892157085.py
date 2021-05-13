if __name__ == '__main__':
    while True:
        data = [int(x) for x in input().split(' ')]
        H = data[0]
        W = data[1]

        if H == 0 and W == 0:
            break

        for i in range(H):
            if i == 0 or i == H-1:
                print('#' * W)
            else:
                print('#' + '.'*(W-2) + '#')
        print('')

