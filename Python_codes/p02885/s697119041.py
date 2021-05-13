input_l = input().rstrip().split(' ')
input_l = list(map(int,input_l))

if(input_l[0] > input_l[1] * 2):
    print(input_l[0]-input_l[1]*2)
else:
    print(0)