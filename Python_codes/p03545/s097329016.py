abcd=str(input())
for i in range(2**4):
    list=[int(abcd[0])]
    symbol=[]
    for j in range(1,4):
        if (i>>j)&1==True:
            list.append(int(abcd[j]))
            symbol.append('+')
        else:
            list.append(int(abcd[j])*(-1))
            symbol.append('-')
    if sum(list)==7:
        print(str(abcd[0])+symbol[0]+str(abcd[1])+symbol[1]+str(abcd[2])+symbol[2]+abcd[3]+"=7")
        break