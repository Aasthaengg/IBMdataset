s = input()
x,y = map(int,input().split())

x_mov = []
y_mov = []

s += "T"
flag = 'x'
mov = 0
for c in s:
    if c=='F':
        mov += 1
    elif flag == 'x':
        flag = 'y'
        x_mov.append(mov)
        mov = 0
    else:
        flag = 'x'
        y_mov.append(mov)
        mov = 0

def get_pos(pos,mov_set):
    for i in mov_set:
        new_pos = set()
        for j in pos:
            new_pos.add(j+i)
            new_pos.add(j-i)
        pos = new_pos
    return pos

if s[0] =="T":
    x_pos = get_pos([0],x_mov)
else:
    x_pos = get_pos([x_mov[0]],x_mov[1:])
y_pos = get_pos([0],y_mov)

print("Yes" if x in x_pos and y in y_pos else "No")