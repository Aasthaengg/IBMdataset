S =input()

if S.count("KIH")==1 and S.replace('A',"")=="KIHBR" and S.count("A")<=4 and S.count("AA")==0:
    print('YES')
else:
    print('NO')