import math
s=int(input())
up=int(math.sqrt(s))+1
if s==1000000000000000000:
    print("0 0 1000000000 0 0 1000000000")
    exit()
print("{} {} {} {} {} {}".format(0,0,1,up,up,up*up-s))