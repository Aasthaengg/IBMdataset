import math
import copy
import time


line1 = str(input()).split(" ")

for index in range(len(line1)):
    line1[index] = int(line1[index])
if (line1[1] > 1 and line1[0] > 1):
    print( line1[0]*line1[1] - (2*line1[1] + 2*(line1[0]-2)))
elif (line1[1] == 1 and line1[0] == 1):
    print(1)
elif (line1[1] == 0 or line1[1] == 0):
    print(0)
else:
    print(line1[0]*line1[1] - 2)
