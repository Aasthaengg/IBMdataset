k = input()
s = list(map(len, k.split("T")))
x, y = map(int, input().split())
x_list = []
y_list = []
check = 1
for i in range(len(s)):
    if check == 1:
        x_list.append(s[i])
        check = -1
    else:
        y_list.append(s[i])
        check = 1

now_x = [x_list[0]]
for move in x_list[1:]:
    nxt = set()
    for i in now_x:
        nxt.add(i + move)
        nxt.add(i - move)
    now_x = nxt
    
now_y = [0]
for move in y_list:
    nxt = set()
    for i in now_y:
        nxt.add(i + move)
        nxt.add(i - move)
    now_y = nxt

if (x in now_x) & (y in now_y):
    print('Yes')
else:
    print('No')