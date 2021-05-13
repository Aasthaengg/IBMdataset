import math
A,B=map(int, input().split())
print (B+A-2*A*math.ceil(B%A/20))