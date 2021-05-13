ROW, COL, K = map(int, input().split())
for row in range(ROW + 1):
    for col in range(COL + 1):
        if row * (COL - col) + col * (ROW - row) == K:
            print('Yes')
            exit()
print('No')
