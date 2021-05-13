n = int(input())

t = [0]*1001001
x = [0]*1001001
y = [0]*1001001


for i in range(n):
    a, b, c = map(int, input().split())
    t[i+1] = a
    x[i+1] = b
    y[i+1] = c

flag = 1    
for  i in range(n):
    dt = t[i+1] - t[i]
    dist = abs(x[i+1]-x[i]) + abs(y[i+1] - y[i])
    if dt < dist:
        flag = 0
    if dist % 2 != dt % 2:
        flag = 0

if flag:
    print("Yes")
else:
    print("No")