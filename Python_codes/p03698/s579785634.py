s = input()
l = list(s)

flag = True
for i in range(len(l) - 1):
    if l[i] in l[i + 1:]:
        flag = False

if flag:
    print('yes')
else:
    print('no')