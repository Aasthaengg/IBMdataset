data = input()
length = len(data)

between = length - 1
num = 0
for i in range(2**between):
    list_data = list(data)
    for j in range(between):
        if ((i >> j) & 1):
            list_data[between - j] = '+'+list_data[between - j]
    hoge = ''.join(list_data).split('+')
    for k in hoge:
        num += int(k)

print(num)