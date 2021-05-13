a_list = ['A', 'B', 'C', 'D', 'E', 'F']
x, y = input().split()
if int(a_list.index(x)) > int(a_list.index(y)):
    print('>')
elif int(a_list.index(x)) < int(a_list.index(y)):
    print('<')
else:
    print('=')
