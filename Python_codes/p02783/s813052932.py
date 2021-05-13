import math
tmp = input().split(" ")
 
HP = int(tmp[0])
attack = int(tmp[1])
 
print(math.ceil(HP/attack))