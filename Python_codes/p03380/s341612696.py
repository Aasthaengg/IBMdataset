import math 

n = int(input())
a = list(map(int, input().split()))

m = max(a)
k = 0

for x in a:
    if abs((k * 2 - m)) > abs((x * 2 - m)):
        k = x

print(m, k)
