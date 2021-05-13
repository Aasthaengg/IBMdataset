flag = 1
all_tes_date = []
jag = []
while flag:
    tes_date = [int(tes) for tes in input().split()]
    if tes_date == [-1,-1,-1]:
        flag = 0
    else:
        all_tes_date.append(tes_date)

for tes_jag in all_tes_date:
    if (tes_jag[0] + tes_jag[1]) > 79:
        jag.append('A')
    elif (tes_jag[0] + tes_jag[1]) > 64:
        jag.append('B')
    elif ((tes_jag[0] + tes_jag[1]) > 49):
        jag.append('C')
    elif (tes_jag[0] + tes_jag[1]) > 29 and not(tes_jag[0] == -1) and not(tes_jag[1] == -1):
        if tes_jag[2] > 49:
            jag.append('C')
        else:
            jag.append('D')
    elif ((tes_jag[0] + tes_jag[1]) < 30) or (tes_jag[0] == -1) or (tes_jag[1] == -1):
        jag.append('F')
        
for jag_rs in jag:
    print(jag_rs)
