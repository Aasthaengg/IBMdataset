def resolve():
    H, W = [int(i) for i in input().split()]
    aa = [input() for _ in range(H)]
    print("".join(["#" for _ in range(W + 2)]))
    for r in range(H):
        print("#" + aa[r] + "#")
    print("".join(["#" for _ in range(W + 2)]))


resolve()
