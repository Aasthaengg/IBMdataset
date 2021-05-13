import math
import numpy as np

def  XYZTriplets():

    num = int(input())
    
    list_num = []
    
    count = [0]*num
    
    for i in range(1, num+1):
        list_num.append(i)

    for x in range(1, int(math.sqrt(num))):
        for y in range(1, int(math.sqrt(num))):
            for z in range(1, int(math.sqrt(num))):
                
                function = x*x + y*y + z*z + x*y + y*z + z*x
                
                if function <= num and function > 0:
                    count[function-1] = count[function-1] + 1
 
    for i in range(0, num):
        print(count[i])
        

if __name__ == '__main__':
    XYZTriplets()
