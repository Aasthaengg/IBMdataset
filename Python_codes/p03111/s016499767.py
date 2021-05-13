n, *abc = [int(x) for x in input().split()]
l = [int(input()) for i in range(n)]
A = 0; B = 1; C = 2;

minmp = 10 ** 9
for k in range(2 ** (2 * n)):
    mat = [[], [], [], []]  # mat[0]:= Aの材料, mat[1]:=Bの材料, mat[2]:=Cの材料
    # for i = 0, ..., N-1
    # kの 2*i & 2*i+1ビット目が 0b00: l[i]はAに使う
    #     ↑lsbから             0b01: l[i]はBに使う
    #                         0b10: l[i]はCに使う
    #                         0b11: l[i]は使わない
    for i in range(n):
        mat[k & (0b11)].append(l[i])
        k >>= 2

    if len(mat[0]) == 0 or len(mat[1]) == 0 or len(mat[2]) == 0:
        continue

    mp = 0
    for j in range(3):
        mp += 10 * (len(mat[j]) - 1)
        mp += 1 * abs(abc[j] - sum(mat[j]))

    minmp = min(minmp, mp)

print(minmp)