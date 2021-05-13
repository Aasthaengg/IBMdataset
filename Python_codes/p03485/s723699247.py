input_number = input().split(' ')
a = float(input_number[0])
b = float(input_number[1])

ave = (a+b)/2

if ave%1 == 0:
    print(int(ave))
else:
    print(int(ave) +1)