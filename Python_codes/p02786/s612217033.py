a=int(input())
import math
total=0
total2=1
while True:
    if a>1:
        a=a//2
        total+=total2
        total2=total2*2
    elif a==1:
        print(total+total2)
        break