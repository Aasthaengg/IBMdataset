S = input()
flag = 0
if S[0] == 'A' and S[2:-1].count('C')==1 :
    if S.replace('A',"").replace('C',"").islower():
        flag =1
        print('AC')
if flag == 0:
    print('WA')