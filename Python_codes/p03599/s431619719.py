a, b, c, d, e, f = map(int, input().split())

a *= 100
b *= 100

#取りうる水の値をリスト化
wat = 0
wat_list = []
for i in range(f//a+1):
    for j in range(f//b+1):
        wat = a*i+b*j
        if 0 < wat <= f:
            wat_list.append(wat)

#水の量に対して砂糖の量をリストで計算
sug = 0
sug_max = 0
sug_list = []
conc_list = []
sug_wat_list = []
for k in wat_list:
    sug_max = k//100 * e
    for l in range(sug_max // c + 1):
        for m in range(sug_max //d + 1):
            sug = c*l+d*m
            if 0<= sug <= sug_max and k+sug <= f: #溶けること＋溢れないこと
                sug_list.append(sug)
                conc_list.append(sug/(sug+k)*100)
                sug_wat_list.append(sug+ k)

idx = conc_list.index(max(conc_list))
print(sug_wat_list[idx], sug_list[idx])