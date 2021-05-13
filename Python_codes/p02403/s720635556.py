if __name__ == '__main__':
    while True:
        data = [int(x) for x in input().split(' ')]
        H = data[0]
        W = data[1]
        assert  0<=H<=300 and 0<=W<=300, "invalid input"

        if H == 0 and W == 0:
            break

        for i in range(H):
            print('#' * W)
        print('')