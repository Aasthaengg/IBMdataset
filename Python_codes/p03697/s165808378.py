num = input().split()
num_i = [int(s) for s in num]

if(num_i[0]+num_i[1] >= 10):
    print('error')
else:
    print(num_i[0]+num_i[1])