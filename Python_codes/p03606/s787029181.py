import io
import math

nancy = int(input())
sam = 0

for i in range(nancy):
    a,b=map(int,input().split())
    sam+=b-a+1

print(sam)