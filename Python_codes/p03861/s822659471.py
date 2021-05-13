import sys


numbers = sys.stdin.readline().split(' ')

a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])


if a > 0:
    print(b//c - (a-1)//c)
else:
    print(b//c+1)



