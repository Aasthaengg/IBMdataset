a = list(map(int,input().split(" ")))
b = list(map(int,input().split(" ")))
c = list(map(int,input().split(" ")))

x = 0
y = 0

for i in range(1,a[0]):
    x = x + b[i] - b[0]
    
xx = x
for i in range(1,a[0]-1):
    xx = xx - ((b[i] - b[i - 1]) * (a[0] - i))
    x = x + xx

for i in range(1,a[1]):
    y = y + c[i] - c[0]
    
yy = y
for i in range(1,a[1]-1):
    yy = yy - ((c[i] - c[i - 1]) * (a[1] - i))
    y = y + yy

ans = x * y
ans = ans % (10**9 + 7)

print(ans)