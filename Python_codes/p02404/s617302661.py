while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    print("\n".join(["".join(["#" if w == 0 or w == W-1 or h == 0 or h == H-1 else "." for w in range(W)]) for h in range(H)])+"\n")