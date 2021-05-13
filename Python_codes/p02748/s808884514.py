# 24
A,B,M = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
Sum = float("inf")
for i in range(M):
    x,y,c = map(int,input().split())
    if a[x-1]+b[y-1]-c < Sum:
        Sum = a[x-1]+b[y-1]-c
    
a.sort()
b.sort()
if a[0]+b[0] < Sum:
    Sum = a[0]+b[0]
print(Sum)