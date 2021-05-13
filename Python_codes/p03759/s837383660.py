from statistics import mean, median,variance,stdev
import sys
import math

x = input().split()
#y = input().split()
a = []
for i in range(len(x)):
   a.append(int(x[i]))
if a[2]-a[1]==a[1]-a[0]:print("YES")
else : print("NO")