s=input().split()
if int(s[2])-int(s[1])==1:
    print('Borys')
elif (int(s[2])-int(s[1]))%2==0:
    print('Alice')
else:
    print('Borys')