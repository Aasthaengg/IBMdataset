num = input().split()
num_i = [int(s) for s in num]

x, a, b = num_i

if(abs(a-x) > abs(b-x)):
    print('B')
else:
    print('A')