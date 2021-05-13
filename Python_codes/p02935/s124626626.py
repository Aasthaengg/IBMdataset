import math

N = int(input())
v = list(map(int, input().split()))
v.sort()
for i in range(N-1):
    v.append( ( v.pop(0) + v.pop(0) ) / 2 )
    v.sort()
print(v[0])


