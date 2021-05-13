o = input()
e = input()
flag = True
if len(o) != len(e):
    flag = False
for i in range(len(o)):
    print(o[i], end='')
    if not flag and i == len(e):
        break
    print(e[i], end='')