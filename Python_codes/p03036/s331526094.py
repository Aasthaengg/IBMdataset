import sys

r,d,x2000 = map(int, input().split())
tmp = x2000
ans = ''

for y in range(2001, 2011):
    result = r * tmp - d
    tmp = result
    print(result)