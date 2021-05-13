n,x,y = map(int,input().split())
max = min(x,y)
if n-(x+y) < 0:
    min = abs(n-x-y)
else:
    min = 0
print(max,min)
