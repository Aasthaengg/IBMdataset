n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

suma = sum(a)
sumb = sum(b)
sousa = sumb-suma

import math
plus1=0
plus2=0
for i in range(n):
    if a[i] < b[i]:
        plus2+=math.ceil((b[i]-a[i])/2)
    elif a[i] > b[i]:
        plus1+=a[i]-b[i]

if plus1<=sousa and plus2<=sousa:
    print("Yes")
else:
    print("No")