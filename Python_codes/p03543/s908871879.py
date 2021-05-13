a=input()
print('YNeos'[not ( a[0]==a[1]==a[2] or a[1]==a[2]==a[3])::2])