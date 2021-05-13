string = input()
numbers = string.split()
W = int(numbers[0])
H = int(numbers[1])
x = int(numbers[2])
y = int(numbers[3])
r = int(numbers[4])
if x-r>=0 and y-r>=0 and x+r<=W and y+r<=H:
    print('Yes')
else:
    print('No')
