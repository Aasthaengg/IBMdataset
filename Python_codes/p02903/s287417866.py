H, W, A, B = map(int, input().split())
res1 = "1" * A + "0" * (W - A)
res2 = "0" * A + "1" * (W - A)
for i in range(H):
    if i < B:
        print(res1)
    else:
        print(res2)
