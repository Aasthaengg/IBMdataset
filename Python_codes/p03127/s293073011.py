n = int(input())

al = list(map(int, input().split())) 

import math

temp = al[0]

for i in range(1,n):
    temp = math.gcd(temp,al[i])
    
print(temp)