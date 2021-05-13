while True:
    H,W = map(int,input().split())
    if 1 <= H and W <= 300:
        print(H * ((W * ('#')) +'\n'))
    else:
        break