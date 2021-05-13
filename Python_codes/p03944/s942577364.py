w,h,n = map(int,input().split())
mode = [[0],[w],[0],[h]]
for i in range(n):
    x,y,a = map(int,input().split())
    if a == 1:
        mode[0].append(x)
    elif a == 2:
        mode[1].append(x)
    elif a == 3:
        mode[2].append(y)
    else:
        mode[3].append(y)
b = [min(mode[1])-max(mode[0]),min(mode[3])-max(mode[2])]
print(b[0]*b[1] if (0 < b[0] and 0 < b[1]) else 0)