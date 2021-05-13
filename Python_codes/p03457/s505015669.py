n = int(input())
l = [[0,0,0]]
for i in range(n):
    t,x,y = map(int,input().split())
    l.append([t,x,y])
for i in range(n):
    t,x,y = l[i][0],l[i][1],l[i][2]
    t_,x_,y_ = l[i+1][0],l[i+1][1],l[i+1][2]
    if t_ - t < (abs(x-x_)+abs(y-y_)) or (t_-t-(abs(x-x_)+abs(y-y_)))%2 != 0:
        print('No')
        exit()
print('Yes')