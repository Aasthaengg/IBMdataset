n = int(input())

ab = 4
af = 3
ar = 10

data = [[[0 for i in range(ar)] for j in range(af)] for k in range(ab)]

for i in range(n):
    instr = input().split()
    b = int(instr[0])
    f = int(instr[1])
    r = int(instr[2])
    v = int(instr[3])

    data[b - 1][f - 1][r - 1] += v

for i in range(ab):
    if i != 0:
        print('#' * 20)
    for j in range(af):
        print("", *data[i][j])

