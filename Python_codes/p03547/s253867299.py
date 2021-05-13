x,y = input().split()
num = ['A', 'B', 'C', 'D', 'E', 'F']
a = num.index(x)
b = num.index(y)
if (a > b):
    print('>')
elif (a == b):
    print('=')
else:
    print('<')