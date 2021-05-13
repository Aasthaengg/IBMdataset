n = int(input())
s = [[0,0,0]]
flag = 0
for i in range(n):
    t, x, y = map(int, input().split())
    s.append([t,x,y])
# print(s)
for i in range(1,n+1):
    dt = s[i][0]-s[i-1][0]
    dx = abs(s[i][1]-s[i-1][1])
    dy = abs(s[i][2]-s[i-1][2])
#     print(dt,dx,dy)
    if dt - (dx+dy) >= 0 and dt % 2 == (dx+dy) % 2:
        continue
    else:
        flag = 1
        print('No')
        break
if flag == 0:
    print('Yes')