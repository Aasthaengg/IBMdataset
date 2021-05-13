a,b,c,d = list(map(int,input()))
op = ['plus','minus']
dic = {'plus':'+','minus':'-'}

for op1 in op:
    for op2 in op:
        for op3 in op:
            ans = a
            if op1 == 'plus':
                ans += b
            else:
                ans -= b
            if op2 == 'plus':
                ans += c
            else:
                ans -= c
            if op3 == 'plus':
                ans += d
            else:
                ans -= d
            if ans == 7:
                print(f'{a}{dic[op1]}{b}{dic[op2]}{c}{dic[op3]}{d}=7')
                exit()

