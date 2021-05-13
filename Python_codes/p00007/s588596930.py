import math
kane=100000
n=int(input())
for i in range (1,n+1):
    syaku=kane*1.05/1000
    kane=math.ceil(syaku)*1000
print(kane)

