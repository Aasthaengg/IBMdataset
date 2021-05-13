def resolve():
    W, H, x, y = [int(i) for i in input().split()]
    if W / 2 == x and H / 2 == y:
        flg = 1
    else:
        flg = 0
    print(*[W * H / 2, flg])


resolve()
