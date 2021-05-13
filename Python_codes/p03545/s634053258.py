ABCD = input()
for i in ('-1','+1'):
    for j in ('-1','+1'):
        for k in ('-1','+1'):
            if int(ABCD[0]) + (int(i)) * int(ABCD[1]) + (int(j)) * int(ABCD[2]) + + (int(k)) * int(ABCD[3]) == 7:
                print(ABCD[0]+i[0]+ABCD[1]+j[0]+ABCD[2]+k[0]+ABCD[3]+'=7')
                exit()
