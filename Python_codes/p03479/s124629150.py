import math
x,y=map(int,input().split())
k=math.floor(math.log2(y/x))

for i in range(k+3):
    if x*(2**i)>y:
        print(i)
        break