import math
p,q= input().split()
a,b =(int(p), int(q))
count = 2*b + 1
print(math.ceil(a/count))