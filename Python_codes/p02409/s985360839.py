n = int(input())
public_hall = [[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]]]
input_info = []

for b in range(4):
    for f in range(3):
        for r in range(10):
            public_hall[b][f].append(0)

for i in range(n):
    input_info.append(input().split())
    input_info[i] = list(map(int, input_info[i]))

for j in range(n):
    public_hall[input_info[j][0] - 1][input_info[j][1] - 1][input_info[j][2] - 1] += input_info[j][3]

for k in range(4):
    for l in range(3):
        for m in range(10):
            print('', public_hall[k][l][m],end='')
        print()
    if k != 3:
        print('#' * 20)