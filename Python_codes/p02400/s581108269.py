#coding: UTF-8
import math

def Circle_Area(r):
    print(format(r*r*math.pi,'.6f'),format(2*r*math.pi,'.6f'))

if __name__=="__main__":
    Circle_Area(float(input()))