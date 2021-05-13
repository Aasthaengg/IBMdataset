
import numpy as np

a,b,c,d=map(int,input().split())
k=a+b-c-d
if(k>0):print("Left")
elif(k==0):print("Balanced")
else:print("Right")
