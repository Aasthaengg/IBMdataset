X, Y = input().split()
dic = ['A', 'B', 'C', 'D', 'E', 'F']
if dic.index(X) < dic.index(Y):
    print('<')
elif dic.index(X) == dic.index(Y):
    print('=')
else:
    print('>')