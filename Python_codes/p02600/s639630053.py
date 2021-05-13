X = int(input())

kyu = [400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000]
for i in range(9):
    if X < kyu[i]:
        print(9 - i)
        exit()
