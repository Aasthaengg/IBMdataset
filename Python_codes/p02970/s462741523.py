N, D = map(int, input().split())
for i in range(20):
    if i * (2 * D + 1) >= N:
        print(i)
        exit()
    else:
        pass