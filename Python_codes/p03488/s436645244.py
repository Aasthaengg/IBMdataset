s = input()
dest_x, dest_y = map(int, input().split())

x_list = []
y_list = []
cnt = 0
flg = 1
init = 1 if s[0] == 'F' else 0
for si in s:
    if si == 'F':
        cnt += 1
    else:
        if flg == 1:
            x_list.append(cnt)
        else:
            y_list.append(cnt)
        cnt = 0
        flg *= -1
if flg == 1:
    x_list.append(cnt)
else:
    y_list.append(cnt)

if init:
    dest_x -= x_list[0]
    x_list[0] = 0

dest_x, dest_y = abs(dest_x), abs(dest_y)

x_max = sum(x_list)
if x_max < dest_x:
    print('No')
    exit()
dpx = [[0 for _ in range(x_max+1)] for _ in range(len(x_list)+1)]
dpx[0][-1] = 1
for i in range(len(x_list)):
    for j in range(x_max+1):
        x = x_list[i]
        if dpx[i][j] == 1:
            if j - 2 * x >= 0:
                dpx[i+1][j-2*x] = 1
            dpx[i+1][j] = 1
if dpx[-1][dest_x] == 0:
    print('No')
    exit()

y_max = sum(y_list)
if y_max < dest_y:
    print('No')
    exit()
dpy = [[0 for _ in range(y_max+1)] for _ in range(len(y_list)+1)]
dpy[0][-1] = 1
for i in range(len(y_list)):
    for j in range(y_max+1):
        y = y_list[i]
        if dpy[i][j] == 1:
            if j - 2 * y >= 0:
                dpy[i+1][j-2*y] = 1
            dpy[i+1][j] = 1
if dpy[-1][dest_y] == 0:
    print('No')
    exit()

print('Yes')
