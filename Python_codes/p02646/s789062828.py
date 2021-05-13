a, v = map(int, input().split())
b, w = map(int, input().split())
T = int(input())
 
k = b - a
flag = False
 
if k >= 0:
    l = T*v - T*w 
    if (k <= l):
        flag = True
 
if k < 0:
    k = a - b
    l = T*v - T*w
    if (k <= l):
        flag = True
 
 
if (flag == True):
    print('YES')
else:
    print('NO')