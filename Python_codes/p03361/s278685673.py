def check(ss, r, c):
    for_chk = ((-1, 0), (0, -1), (0, 1), (1, 0))
    H = len(ss)
    W = len(ss[0])
    for ri, ci in for_chk:
        rc = r + ri
        cc = c + ci
        if 0 <= rc and rc < H and 0 <= cc and cc < W:
            if ss[rc][cc] == "#":
                return True
    return False


def resolve():
    H, W = [int(i) for i in input().split()]
    ss = [list(input()) for _ in range(H)]
    for r in range(H):
        for c in range(W):
            if ss[r][c] == "#":
                if not check(ss, r, c):
                    print("No")
                    return
    print("Yes")


resolve()
