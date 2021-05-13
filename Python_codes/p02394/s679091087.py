if __name__ == '__main__':
    key_in = input()
    data = key_in.split(' ')

    # ???????????? W, H, x, y, r ??????
    W = int(data[0])
    H = int(data[1])
    x = int(data[2])
    y = int(data[3])
    r = int(data[4])

    result = False
    if r <= x <= W-r and r <= y <= H-r:
        result = True

    if result is True:
        print('Yes')
    else:
        print('No')