import math

# inputList=[]
# for i in range(6):
#     inputNum = input()
#     inputList.append(inputNum)
inputa = input().split()
# inputb = input().split()

# inputa = [int(n) for n in inputa]
# inputa.sort()

a = int(inputa[0])
# b = int(inputa[1])
# c = int(inputa[2])

# x = int(inputb[0])
# y = int(inputb[1])


if a < 1200:
    print("ABC")
elif a < 2800:
    print("ARC")
else:
    print("AGC")