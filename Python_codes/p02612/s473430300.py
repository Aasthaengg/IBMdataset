import math
n = int(input())
i = 1
while(1):
    if 1000*i - n >= 0:
        print(1000*i - n)
        break
    else:
        i += 1