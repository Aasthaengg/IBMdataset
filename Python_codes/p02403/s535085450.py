H, W = map(int, raw_input().split())
while H | W != 0:
    for i in range(H):
        print '#' * W
    print ''
    H, W = map(int, raw_input().split())