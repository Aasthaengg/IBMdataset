import math

a=list(map(int,input().split()))
print(min(math.floor(a[1]/a[0]),a[2]))