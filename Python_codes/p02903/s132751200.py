H, W, A, B = map(int, input().split())

for H in range(H):
    if H < B:
        line = '0' * A + '1' * (W-A)
    else:
        line = '1' * A + '0' * (W-A)
    print(line)