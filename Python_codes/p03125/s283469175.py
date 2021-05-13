list1 = [i for i in input().split()]

num1 = int(list1[0])
num2 = int(list1[1])

if num2 % num1 == 0:
    print (num1+num2)
else:
    print (num2-num1)