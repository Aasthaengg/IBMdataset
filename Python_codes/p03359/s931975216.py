num = input().split()
num_i = [int(s) for s in num]

if(num_i[1] >= num_i[0]):
    print(num_i[0])
else:
    print(num_i[0]-1)    