import math
from decimal import *

n = int(input())
nos = list(map(int, input().split()))
arr = [0 for i in range(n)]
if(n>1):
    arr[1] = abs(nos[1]-nos[0])
for i in range(2, n):
    a ,b = abs(nos[i]-nos[i-1])+arr[i-1], abs(nos[i]-nos[i-2])+arr[i-2]
    if(a>b):
        arr[i]=b
    else:
        arr[i] = a
print(arr[n-1])