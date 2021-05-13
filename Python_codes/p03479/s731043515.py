X, Y = map(int, input().split())

# 2 倍していってYを越えたら終わり
for i in range(100):
    if X * 2**i > Y:
        print(i)
        exit()
