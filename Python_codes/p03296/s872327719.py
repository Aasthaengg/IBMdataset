import sys  
import numpy as np

input = sys.stdin.readline
A = int(input())
a = list(map(int, input().split()))
sum1 = 0
for i in range(1,A):
    if a[i-1] == a[i]:
        sum1+=1
        a[i] = 0

print(sum1)