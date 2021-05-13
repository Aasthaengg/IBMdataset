a,b,c,d = map(int,input().split())
d1 = a-b; d2 = c-b; d3 = a-c

if d1 < 0:
    d1 = -d1
if d2 < 0:
    d2 = -d2 
if d3 < 0:
    d3 = -d3

if d1 <= d and d2 <= d or d3 <= d:
    print('Yes')
else:
    print('No')