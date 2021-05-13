import math

# inputList=[]
# for i in range(6):
#     inputNum = input()
#     inputList.append(inputNum)
inputa = input().split()
# inputb = input().split()

a = int(inputa[0])
b = int(inputa[1])
# c = int(inputa[2])

# x = int(inputb[0])
# y = int(inputb[1])

if b % a == 0:
    print(a+b)
else:
    print(b-a)
