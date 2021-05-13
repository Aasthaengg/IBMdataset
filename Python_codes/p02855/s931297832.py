h, w, k = map(int, input().split())
cake = []
piece = []
flg = False
for _ in range(h):
    s = input()
    if flg and s.count("#") != 0:
        cake.append(piece)
        piece = [s]
        continue
    piece.append(s)
    if s.count("#") != 0:
        flg = True
cake.append(piece)

cnt = 0
for ps in cake:
    r = len(ps)
    oo = [0] * w
    for p in ps:
        st = p.count("#")
        if st == 0:
            continue
        cnt += 1
        for i, v in enumerate(p):
            oo[i] = cnt
            if v == "#":
                if st == 1:
                    pass
                else:
                    cnt += 1
                    st -= 1
    for _ in range(r):
        print(*oo)