import math

S=100000
n=int(input())

for i in range(n):
    S*=1.05
    s=S/1000
    ceilnum = math.ceil(s)
    S=ceilnum*1000 

print(S)
