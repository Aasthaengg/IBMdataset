H, W, A, B = map(int, input().split())

for i in range(H):
    row = []
    for j in range(W):
        if ((i < B and j < A) or (B <= i and A <= j)):
            row.append('0')
        else:
            row.append('1')
    print(''.join(row))
