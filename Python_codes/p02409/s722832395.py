res = ['-']
for mak in range(12) :
    tem = ['0' for temp in range(10)]
    res.append(tem)

for mak in range(int(input())) :
    a, b, c, d    = [int(temp) for temp in input().split()]
    res[((a - 1) * 3) + b][c - 1] = str(int(res[((a - 1) * 3) + b][c - 1]) + d)

for mak in range(1,13) :
    if mak != 1 and mak % 3 == 1 :
        print(('#' * 20))
    print('', ' '.join(res[mak]))