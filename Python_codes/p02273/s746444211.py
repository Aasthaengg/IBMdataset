import math

n = int(input())



def koch(n,x_0,y_0,x_1,y_1):
    if n == 0:
        return    
    x_m1 = x_0 + (x_1- x_0)/3
    y_m1 = y_0 + (y_1 -y_0)/3
    x_m2 = x_0 + (x_1- x_0)* 2/3
    y_m2 = y_0 + (y_1 -y_0) *2/3
    x_m =  (x_m2 - x_m1) * math.cos(math.pi/3) - (y_m2 - y_m1) * math.sin(math.pi/3) + x_m1
    y_m =  (x_m2 - x_m1) * math.sin(math.pi/3) + (y_m2 - y_m1) * math.cos(math.pi/3) + y_m1

    koch(n-1,x_0,y_0,x_m1,y_m1)
    print(x_m1,y_m1)
    koch(n-1,x_m1,y_m1,x_m,y_m)
    print(x_m,y_m)
    koch(n-1,x_m,y_m,x_m2,y_m2)
    print(x_m2,y_m2)
    koch(n-1,x_m2,y_m2,x_1,y_1)
    
print(0,0)
koch(n,0,0,100,0)
print(100,0)