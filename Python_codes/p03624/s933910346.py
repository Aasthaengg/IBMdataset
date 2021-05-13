s=input()
f=1
for i in 'abcdefghijklmnopqrstuvwxyz':
    if i not in s:
        print(i)
        f=0
        exit()
if f:print('None')