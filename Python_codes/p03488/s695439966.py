s = input()
x, y = map(int, input().split())
X = 0
num = 0
while num <= len(s) - 1:
    if s[num] == "F":
        X += 1
        num += 1
    else:
        num += 1
        break
flag = False
move_x = []
move_y = []
temp = 0
while num <= len(s) - 1:
    if s[num] == "F":
        temp += 1
        num += 1
    else:
        if flag == False:
            move_y.append(temp)
            flag = True
        else:
            move_x.append(temp)
            flag = False
        num += 1
        temp = 0
else:
    if flag == False:
        move_y.append(temp)
    else:
        move_x.append(temp)
set_x = {X}
set_y = {0}
for i in move_x:
    temp = set()
    for j in set_x:
        temp.add(j + i)
        temp.add(j - i)
    set_x = temp
for i in move_y:
    temp = set()
    for j in set_y:
        temp.add(j + i)
        temp.add(j - i)
    set_y = temp
if x in set_x and y in set_y:
    print("Yes")
else:
    print("No")