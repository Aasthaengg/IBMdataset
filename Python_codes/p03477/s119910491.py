num = input().split()
num_i = [int(s) for s in num]

if((num_i[0]+num_i[1]) > (num_i[2]+num_i[3])):
    print('Left')
elif((num_i[0]+num_i[1]) == (num_i[2]+num_i[3])):
    print('Balanced')
else:
    print('Right')