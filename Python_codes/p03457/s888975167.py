n = int(input())
TP = [[0, 0, 0]]
for _ in range(n):
    TP.append(list(map(int, input().split())))
for i in range(1, n + 1):
    td = TP[i][0] - TP[i-1][0]
    pd = abs(TP[i][1] - TP[i-1][1]) + abs(TP[i][2] - TP[i-1][2])
    if td >= pd and td % 2 == pd % 2:
        continue
    else:
        print('No')
        exit()
print('Yes')