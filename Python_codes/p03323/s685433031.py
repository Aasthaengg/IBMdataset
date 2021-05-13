num = input().split()
num_i = [int(s) for s in num]

if(num_i[0] > 8 or num_i[1] > 8):
    print(':(')
else:
    print('Yay!')