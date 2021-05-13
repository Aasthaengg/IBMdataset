s = input()
a = int(s[0])
b = int(s[1])
c = int(s[2])
d = int(s[3])

for i in [-1,1]:
    for j in [-1,1]:
        for k in [-1,1]:
            if a + i*b + j*c + k*d == 7:
                op1 = ['-','+'][i==1]
                op2 = ['-','+'][j==1]
                op3 = ['-','+'][k==1]
                print(f'{a}{op1}{b}{op2}{c}{op3}{d}=7')
                exit()