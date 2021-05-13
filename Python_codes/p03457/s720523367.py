N = int(input())

pos_x=0
pos_y=0
t_now=0
flg = True
for i in range(N):
    t,x,y = map(int,input().split())
    t_del = t-t_now
    res = (t_del-abs(pos_x-x)-abs(pos_y-y))
    if (res>=0) & (res%2==0):
        t_now = t
        pos_x = x
        pos_y=y
        pass
    else:
        flg = False
        break

if flg == True:
    print('Yes')
else:
    print('No')