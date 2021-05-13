x,y = map(str, input().split())
num = ['A','B','C','D','E','F']
for i in num:
    if x == i:
        x = num.index(i)
    if y == i:
        y = num.index(i)
if x == y:
    print('=')
elif x < y:
    print('<')
else:
    print('>')