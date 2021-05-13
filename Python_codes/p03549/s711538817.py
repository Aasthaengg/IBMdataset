import math
n,m = map(int, input().split())
count = math.pow(2,m)
print(int(100*(n-m)*count + 1900*m*count))