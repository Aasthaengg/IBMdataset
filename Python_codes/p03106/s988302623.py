import sys
import math

input = sys.stdin.readline

A,B,K = list(map(int,input().split()))
counter = []
num = 0
while num <101:
    num += 1
    if A %num ==0 and B % num ==0:
        counter.append(num)
    
print(counter[-K])
