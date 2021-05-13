n=int(input())
i=1
s=100000//1000
import math
while i <= n:
    i+=1
    s = s*1.05
    s = math.ceil(s)
    
print(s*1000)

