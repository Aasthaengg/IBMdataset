abcd = input() #4つの数字をstr型で入力
l = len(abcd)  # l=4

for bit in range(1 << l-1):
    N = abcd[0]
    for i in range(3):
        N += ' '
        if ((bit >> i) & 1):
            N += '-'
        else:
            N += '+'
        N += abcd[i+1]
        N += ' '
    #print(N)
    N_int = sum(map(int, N.split()))
    #print(N_int)
    if N_int == 7:
        #ans = list(map(str, N.split()))
        ans = N.replace(' ', '')
        print('{}=7'.format(ans))
        break