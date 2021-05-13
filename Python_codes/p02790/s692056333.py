a,b = input().split()
x = ''
y = ''
for i in range(int(b)):
    x += a
for i in range(int(a)):
    y += b
print(min(x,y))