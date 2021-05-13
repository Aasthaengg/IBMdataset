
from math import *
n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
p_1 = 0
p_2 = 0
p_3 = 0
p_inf = []
for i in range(n):
        p_1 += abs(x[i]-y[i])
        p_2 += pow(abs(x[i]-y[i]),2)
        p_3 += pow(abs(x[i]-y[i]),3)
        p_inf.append(abs(x[i]-y[i]))
print("%f" %p_1)
print("%f" %(sqrt(p_2)))
print("%f" %(pow(p_3,1/3)))
print("%f" %(max(p_inf)))

