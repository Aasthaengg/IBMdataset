if __name__ == '__main__':
    W, H, x, y, r = [int(i) for i in input().split()]
    if (r <= x <= W-r) and (r <= y <= H-r):
        print('Yes')
    else:
        print('No')