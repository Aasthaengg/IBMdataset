h, w = map(int, input().split())
n = int(input())
a = list(map(int,input().split()))

area = [[0 for i in range(w)] for i in range(h)]
num = 1
count = 0

for i in range(h):
    if i % 2 == 0:
        for j in range(w):
            area[i][j] = num
            count += 1
            if count == a[num-1]:
                num += 1
                count = 0
    else:
        for j in range(w-1, -1, -1):
            area[i][j] = num
            count += 1
            if count == a[num - 1]:
                num += 1
                count = 0

for i in range(h):
    for j in range(w):
        print(area[i][j], end=' ')
        if j == w-1:
            print()