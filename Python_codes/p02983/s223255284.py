L, R = [int(i) for i in input().split()]
min = 1 << 30
for i in range(L, R + 1):
    if i % 2019 == 0:
        print(0)
        exit()
L %= 2019
R %= 2019
for i in range(L, R):
    for j in range(i + 1, R + 1):
        if i * j % 2019 < min:
            min = i*j % 2019
print(min)
