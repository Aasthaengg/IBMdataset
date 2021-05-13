from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math
import random
########################################################
bool=False
p=0
for _ in range(int(input())):
    a,b=INPUT()
    if a==b:
        p+=1
    else:
        p=0
    if p>=3:
        bool=True
if bool:
    print("Yes")
else:
    print("No")
