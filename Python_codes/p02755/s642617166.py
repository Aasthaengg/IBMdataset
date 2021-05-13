a, b = map(int, input().split())

for i in range(1, 1251):
    aa = (i * 0.08) // 1
    bb = (i * 0.1) // 1
    if aa == a and bb == b:
        print(i)
        exit()
print(-1)